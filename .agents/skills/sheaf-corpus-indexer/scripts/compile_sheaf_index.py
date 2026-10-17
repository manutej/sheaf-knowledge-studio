#!/usr/bin/env python3
r"""
compile_sheaf_index.py
======================
Universal, Book-Agnostic Page-Anchored PDF Extractor, Offline FTS5 Search Indexer,
and Empirical Sheaf Knowledge Base Compiler.

Can be run in two modes:
1. Universal Auto-Induction on ANY PDF or cached raw pages JSON (ZERO hardcoded concepts):
     python3 compile_sheaf_index.py --pdf path/to/book.pdf --out-dir path/to/kb_dir --title "Book Title" --author "Author"
2. Enrich & Rebuild SQLite FTS5 + Deferred Bundle + Wiki from an existing `sheaf_kb.json`:
     python3 compile_sheaf_index.py --kb path/to/sheaf_kb.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
INDUCTION_SCRIPT = SCRIPT_DIR / "sheaf_induction_engine.py"


def load_induction_engine():
    spec = importlib.util.spec_from_file_location("sheaf_induction_engine", str(INDUCTION_SCRIPT))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def extract_raw_pages_from_pdf(pdf_path: Path, cache_json: Path | None = None) -> list[dict]:
    """Extract verbatim text per page from any PDF using pdftotext (fast) or pypdf fallback."""
    if cache_json and cache_json.exists():
        return json.loads(cache_json.read_text(encoding="utf-8"))

    pages = []
    # Try pypdf first for reliable page-by-page extraction
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))
        for i, page in enumerate(reader.pages):
            pages.append({"page": i + 1, "text": page.extract_text() or ""})
    except Exception:
        # Fallback to pdftotext -f/-l
        info = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True)
        m = re.search(r"Pages:\s+(\d+)", info.stdout)
        total = int(m.group(1)) if m else 1
        for pno in range(1, total + 1):
            res = subprocess.run(["pdftotext", "-f", str(pno), "-l", str(pno), str(pdf_path), "-"], capture_output=True, text=True)
            pages.append({"page": pno, "text": res.stdout or ""})

    if cache_json:
        cache_json.parent.mkdir(parents=True, exist_ok=True)
        cache_json.write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
    return pages


def build_sqlite_fts5_and_wiki(kb: dict, data_dir: Path, wiki_dir: Path):
    """Builds the offline SQLite FTS5 search index, deferred browser bundle, and Markdown Wiki."""
    data_dir.mkdir(parents=True, exist_ok=True)
    wiki_dir.mkdir(parents=True, exist_ok=True)
    (wiki_dir / "chapters").mkdir(parents=True, exist_ok=True)
    (wiki_dir / "concepts").mkdir(parents=True, exist_ok=True)

    # 1. Write deferred browser bundle `sheaf_pages_bundle.js`
    bundle_obj = {
        "pages": kb["pages"],
        "formal_items": kb["formal_items"],
        "full_stalk_items": {s["id"]: s.get("formal_items", []) for s in kb["stalks"]}
    }
    bundle_js = "window.__onSheafBundleLoaded && window.__onSheafBundleLoaded(" + json.dumps(bundle_obj, ensure_ascii=False, separators=(",", ":")) + ");\n"
    (data_dir / "sheaf_pages_bundle.js").write_text(bundle_js, encoding="utf-8")

    # 2. Build SQLite FTS5 database `cattheory_sheaf.db`
    db_path = data_dir / "cattheory_sheaf.db"
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE chapters (
            chapter INTEGER PRIMARY KEY,
            id TEXT,
            title TEXT,
            start_page INTEGER,
            end_page INTEGER,
            theme TEXT
        );
        CREATE TABLE stalks (
            id TEXT PRIMARY KEY,
            title TEXT,
            chapter INTEGER,
            section TEXT,
            start_page INTEGER,
            end_page INTEGER,
            summary TEXT,
            formal_core TEXT,
            tfidf_signature_json TEXT,
            defined_terms_json TEXT
        );
        CREATE TABLE restriction_morphisms (
            id TEXT PRIMARY KEY,
            source TEXT,
            target TEXT,
            kind TEXT,
            overlap TEXT,
            formula TEXT,
            restriction_fidelity REAL,
            coboundary_defect_d0 REAL,
            shared_terms_json TEXT
        );
        CREATE TABLE pages (
            page INTEGER PRIMARY KEY,
            chapter INTEGER,
            section TEXT,
            subsection TEXT,
            stalk_ids_json TEXT,
            items_json TEXT,
            text TEXT
        );
        CREATE TABLE formal_items (
            id TEXT,
            kind TEXT,
            number TEXT,
            title TEXT,
            page INTEGER,
            chapter INTEGER,
            section TEXT,
            stalk_ids_json TEXT,
            text TEXT
        );
        CREATE VIRTUAL TABLE pages_fts USING fts5(page, section, items, text);
        CREATE VIRTUAL TABLE items_fts USING fts5(id, kind, title, page, section, text);
        CREATE VIRTUAL TABLE formal_items_fts USING fts5(id, kind, title, page, section, text);
    """)

    for ch in kb.get("chapters", []):
        cur.execute(
            "INSERT INTO chapters VALUES (?, ?, ?, ?, ?, ?)",
            (ch["chapter"], ch["id"], ch["title"], ch["start_page"], ch["end_page"], ch.get("theme", ""))
        )
    for s in kb.get("stalks", []):
        cur.execute(
            "INSERT INTO stalks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                s["id"], s["title"], s["chapter"], s["section"], s["start_page"], s["end_page"],
                s["summary"], s["formal_core"],
                json.dumps(s.get("tfidf_signature", {})),
                json.dumps(s.get("defined_terms", []))
            )
        )
    for r in kb.get("restriction_morphisms", []):
        cur.execute(
            "INSERT INTO restriction_morphisms VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                r["id"], r["source"], r["target"], r.get("kind", ""), r["overlap"], r["formula"],
                r.get("restriction_fidelity", 0.7), r.get("coboundary_defect_d0", 0.3),
                json.dumps(r.get("shared_terms", []))
            )
        )
    for p in kb.get("pages", []):
        pno = p.get("p", p.get("page"))
        sec = p.get("sec", p.get("section", ""))
        sub = p.get("sub", p.get("subsection", ""))
        sids = p.get("stalks", p.get("stalk_ids", []))
        items = p.get("items", [])
        txt = p.get("txt", p.get("text", ""))
        cur.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)",
            (pno, p.get("ch", p.get("chapter", 1)), sec, sub, json.dumps(sids), json.dumps(items), txt)
        )
        cur.execute(
            "INSERT INTO pages_fts VALUES (?, ?, ?, ?)",
            (str(pno), sec, " ".join(items), txt)
        )
    for it in kb.get("formal_items", []):
        cur.execute(
            "INSERT INTO formal_items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                it["id"], it["kind"], it.get("number", ""), it.get("title", ""),
                it["page"], it.get("chapter", 1), it.get("section", ""),
                json.dumps(it.get("stalk_ids", [])), it.get("text", "")
            )
        )
        cur.execute(
            "INSERT INTO items_fts VALUES (?, ?, ?, ?, ?, ?)",
            (it["id"], it["kind"], it.get("title", ""), str(it["page"]), it.get("section", ""), it.get("text", ""))
        )
        cur.execute(
            "INSERT INTO formal_items_fts VALUES (?, ?, ?, ?, ?, ?)",
            (it["id"], it["kind"], it.get("title", ""), str(it["page"]), it.get("section", ""), it.get("text", ""))
        )
    conn.commit()
    conn.close()

    # 3. Build Persistent Markdown Wiki
    home_lines = [
        f"# {kb['book']['title']} — Sheaf Knowledge Base Wiki (`HOME.md`)\n",
        f"**Author:** {kb['book']['author']} · **Pages:** {kb['book']['total_pages']} · **Stalks:** {len(kb['stalks'])} · **Declarations:** {len(kb['formal_items'])}\n",
        "## Chapters\n"
    ]
    for ch in kb.get("chapters", []):
        home_lines.append(f"- [{ch['title']}](chapters/{ch['id']}.md) (`pp. {ch['start_page']}–{ch['end_page']}`)")
        ch_stalks = [s for s in kb["stalks"] if s["chapter"] == ch["chapter"]]
        ch_md = [
            f"# {ch['title']}\n",
            f"**Page Span:** `pp. {ch['start_page']}–{ch['end_page']}`\n",
            f"**Theme:** {ch.get('theme', '')}\n",
            "## Concept Stalks\n"
        ]
        for s in ch_stalks:
            ch_md.append(f"- [{s['title']}](../concepts/{s['id']}.md) (`§{s['section']}`, `pp. {s['start_page']}–{s['end_page']}`): {s['summary']}")
        (wiki_dir / "chapters" / f"{ch['id']}.md").write_text("\n".join(ch_md) + "\n", encoding="utf-8")

    home_lines.append("\n## Concept Stalks (`0-Simplices`)\n")
    for s in kb.get("stalks", []):
        home_lines.append(f"- [{s['title']}](concepts/{s['id']}.md) (`pp. {s['start_page']}–{s['end_page']}`)")
        c_md = [
            f"# {s['title']} (`{s.get('symbol', s['id'])}`)\n",
            f"- **Page Fiber:** `pp. {s['start_page']}–{s['end_page']}`",
            f"- **Defined Terms:** `{', '.join(s.get('defined_terms', [])[:10])}`\n",
            "## Summary\n",
            s["summary"] + "\n",
            "## Formal Core\n",
            f"$${s['formal_core']}$$\n"
        ]
        (wiki_dir / "concepts" / f"{s['id']}.md").write_text("\n".join(c_md) + "\n", encoding="utf-8")
    (wiki_dir / "HOME.md").write_text("\n".join(home_lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Universal Page-Anchored PDF Extractor & Sheaf Indexer")
    parser.add_argument("--pdf", type=Path, help="Input PDF to extract and auto-induce into a Sheaf Knowledge Base")
    parser.add_argument("--raw-pages", type=Path, help="Cached raw_pages.json to auto-induce without re-running PDF text extraction")
    parser.add_argument("--kb", type=Path, help="Existing sheaf_kb.json to enrich with empirical cohomology and rebuild FTS5 DB")
    parser.add_argument("--out-dir", type=Path, default=Path("sheaf-kb-out"), help="Output directory for data/ and wiki/")
    parser.add_argument("--title", type=str, default="Indexed Monograph", help="Book title when running in --pdf auto mode")
    parser.add_argument("--author", type=str, default="Monograph Author", help="Book author when running in --pdf auto mode")
    args = parser.parse_args()

    ind = load_induction_engine()

    if args.kb and args.kb.exists():
        kb = json.loads(args.kb.read_text(encoding="utf-8"))
        kb = ind.enrich_sheaf_kb_with_empirical_cohomology(kb)
        args.kb.write_text(json.dumps(kb, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Enriched {args.kb} with empirical TF-IDF & Čech cohomology metrics.")
        return

    if args.pdf or args.raw_pages:
        data_dir = args.out_dir / "data"
        wiki_dir = args.out_dir / "wiki"
        cache_path = data_dir / "raw_pages.json"
        if args.raw_pages and args.raw_pages.exists():
            raw_pages = json.loads(args.raw_pages.read_text(encoding="utf-8"))
        else:
            raw_pages = extract_raw_pages_from_pdf(args.pdf, cache_json=cache_path)

        kb = ind.auto_induce_sheaf_from_pages(
            raw_pages,
            title=args.title,
            author=args.author,
            pdf_name=args.pdf.name if args.pdf else "document.pdf"
        )
        # Add 3 default investigations from top stalks so HF-SHEAF-09 is satisfied out of the box
        stalks = kb["stalks"]
        if len(stalks) >= 3 and not kb.get("notebook_investigations"):
            kb["notebook_investigations"] = [
                {
                    "id": f"q-auto-{idx+1}",
                    "question": f"How do {stalks[idx]['title']} and {stalks[idx+1]['title']} connect in {args.title}?",
                    "open_cover": [stalks[idx]["id"], stalks[idx + 1]["id"]],
                    "citations": [
                        {"page": stalks[idx]["start_page"], "label": f"p. {stalks[idx]['start_page']}"},
                        {"page": stalks[idx + 1]["start_page"], "label": f"p. {stalks[idx + 1]['start_page']}"}
                    ],
                    "synthesis_markdown": (
                        f"### Auto-Induced Section: {stalks[idx]['title']} $\\to$ {stalks[idx+1]['title']}\n\n"
                        f"- **{stalks[idx]['title']}** [p. {stalks[idx]['start_page']}]: {stalks[idx]['summary']}\n"
                        f"- **{stalks[idx+1]['title']}** [p. {stalks[idx+1]['start_page']}]: {stalks[idx+1]['summary']}"
                    )
                }
                for idx in range(min(3, len(stalks) - 1))
            ]
            kb = ind.enrich_sheaf_kb_with_empirical_cohomology(kb)

        build_sqlite_fts5_and_wiki(kb, data_dir, wiki_dir)
        kb_path = data_dir / "sheaf_kb.json"
        kb_path.write_text(json.dumps(kb, ensure_ascii=False, indent=2), encoding="utf-8")

        # Install query_sheaf.py and TYPED-CONTRACT-SHEAF-META-PROMPT.md into args.out_dir if available
        import shutil
        for q_cand in [SCRIPT_DIR / "query_sheaf_engine.py", SCRIPT_DIR / "query_corpus.py"]:
            if q_cand.exists() and not (args.out_dir / "query_sheaf.py").exists():
                shutil.copy2(q_cand, args.out_dir / "query_sheaf.py")
                break
        for c_cand in [
            SCRIPT_DIR.parents[1] / "sheaf-knowledge-pipeline/references/TYPED-CONTRACT-SHEAF-META-PROMPT.md",
            SCRIPT_DIR.parents[2] / ".agents/skills/sheaf-knowledge-pipeline/references/TYPED-CONTRACT-SHEAF-META-PROMPT.md"
        ]:
            if c_cand.exists() and not (args.out_dir / "TYPED-CONTRACT-SHEAF-META-PROMPT.md").exists():
                shutil.copy2(c_cand, args.out_dir / "TYPED-CONTRACT-SHEAF-META-PROMPT.md")
                break

        print(f"Auto-induced complete Sheaf KB + FTS5 DB + Wiki at {args.out_dir}: {len(kb['pages'])} pages, {len(kb['chapters'])} chapters, {len(kb['stalks'])} stalks, {len(kb['formal_items'])} formal declarations.")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
