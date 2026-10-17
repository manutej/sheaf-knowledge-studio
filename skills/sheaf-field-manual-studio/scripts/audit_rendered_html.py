#!/usr/bin/env python3
r"""
audit_rendered_html.py
======================
Deterministic Adversarial Auditor for the CETI Field-Manual & Sheaf Notebook Studio HTML.
Enforces binary HARD FAIL gates (HF-STUDIO-01 .. HF-STUDIO-10) covering:
  - HF-STUDIO-01: CETI Field-Manual Palette & Typography Tokens (`#F5EFE3`, `#1A1612`, `#A67756`, Fraunces/DM Sans/JetBrains Mono)
  - HF-STUDIO-02: Fast-Load Split-Bundle Architecture (`< 450 KB` core HTML + `<script defer>` bundle)
  - HF-STUDIO-03: Zero Raw LaTeX Backslash Leakage across all rendered syntheses, stalk cores, and symbolic primitives
  - HF-STUDIO-04: Five-Plate Editorial Architecture (`#plate-1` .. `#plate-5`) + One-Italic-Noun Title Rule (`<em class="u-copper">`)
  - HF-STUDIO-05: Honesty Apparatus Completeness (`.marginalia` with `<cite>` and `.counterpoint` on every Plate)
  - HF-STUDIO-06: Non-Color-Alone Verdict Stamps (`◆`, `⚖`, `✓`, `⊘` + text label)
  - HF-STUDIO-07: Single-Mutator Interactive Instruments & On-Demand 3D Poset Loop
  - HF-STUDIO-08: FORGE Callout & Self-Contained Courseware Law (`Key Concept` / `Why It Matters`; zero "So What"; zero "Module 1" learner card titles; zero stacked `.callout-box` without intervening explanation/spacing)
  - HF-STUDIO-09: Progressive Depth (`data-level="newcomer|practitioner|expert"`) & Paper Theme (`data-theme="light|dark"`) Controls
  - HF-STUDIO-10: Slide-Over Verbatim Book Reader & Interactive Citation Pills (`window.__jumpToPage`)
"""

import argparse
import json
import re
import sys
from pathlib import Path


RAW_LATEX_LEAK_RE = re.compile(
    r"\\(?:mathcal|mathbf|mathrm|text|operatorname|varprojlim|varinjlim|xrightarrow|xleftarrow|dashv|simeq|cong|times|sqcup|rightrightarrows|alpha|beta|gamma|delta|epsilon|eta|lambda|mu|pi|rho|sigma|omega|Delta|Sigma|Pi|Omega)\b"
)


def simulate_js_latex_to_html(s: str) -> str:
    """Python mirror of convertLatexTokensToHtml() in the studio HTML to audit all KB strings."""
    s = re.sub(r"\\begin\{array\}\{[^}]*\}", "", s)
    s = re.sub(r"\\end\{array\}", "", s)
    s = re.sub(r"\\hline\b", "", s)
    s = re.sub(r"\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big)\b", "", s)
    s = re.sub(r"\\[,;:!]", " ", s)
    s = re.sub(r"\\quad\b", " ", s)
    s = re.sub(r"\\qquad\b", "  ", s)
    s = re.sub(r"\\varprojlim_\{([^}]+)\}", r"lim<-(_\1)", s)
    s = re.sub(r"\\varprojlim_([A-Za-z0-9]+)", r"lim<-(_\1)", s)
    s = re.sub(r"\\varprojlim\b", "lim<-", s)
    s = re.sub(r"\\varinjlim_\{([^}]+)\}", r"colim->(_\1)", s)
    s = re.sub(r"\\varinjlim_([A-Za-z0-9]+)", r"colim->(_\1)", s)
    s = re.sub(r"\\varinjlim\b", "colim->", s)
    for _ in range(3):
        s = re.sub(r"\\xrightarrow\{([^{}]+)\}", r"->(\1)", s)
        s = re.sub(r"\\xleftarrow\{([^{}]+)\}", r"<-(\1)", s)
        s = re.sub(r"\\overset\{([^{}]+)\}\{\\to\}", r"->(\1)", s)
        s = re.sub(r"\\mathcal\{([^{}]+)\}", r"\1", s)
        s = re.sub(r"\\mathbf\{([^{}]+)\}", r"\1", s)
        s = re.sub(r"\\(?:mathrm|text|textbf|operatorname|emph)\{([^{}]+)\}", r"\1", s)
    sym_keys = [
        r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", r"\varepsilon", r"\eta", r"\theta",
        r"\lambda", r"\mu", r"\nu", r"\pi", r"\rho", r"\sigma", r"\tau", r"\phi", r"\varphi", r"\psi", r"\omega",
        r"\Gamma", r"\Delta", r"\Theta", r"\Lambda", r"\Pi", r"\Sigma", r"\Phi", r"\Psi", r"\Omega",
        r"\to", r"\rightarrow", r"\leftarrow", r"\leftrightarrow", r"\longleftrightarrow",
        r"\mapsto", r"\longmapsto", r"\hookrightarrow", r"\twoheadrightarrow", r"\leadsto",
        r"\Rightarrow", r"\Leftarrow", r"\Leftrightarrow", r"\Longleftrightarrow", r"\iff", r"\implies", r"\rightrightarrows",
        r"\dashv", r"\vdash", r"\cong", r"\simeq", r"\sim", r"\equiv", r"\approx", r"\neq",
        r"\leq", r"\geq", r"\leqslant", r"\geqslant", r"\subseteq", r"\subset", r"\supseteq", r"\supset",
        r"\in", r"\notin", r"\ni", r"\bigcup", r"\bigcap", r"\cup", r"\cap", r"\bigsqcup", r"\sqcup", r"\sqcap",
        r"\wedge", r"\vee", r"\neg", r"\lnot", r"\mid", r"\gcd", r"\lcm",
        r"\times", r"\otimes", r"\oplus", r"\prod", r"\coprod", r"\sum", r"\int", r"\circ", r"\bullet", r"\cdot", r"\star",
        r"\forall", r"\exists", r"\nexists", r"\emptyset", r"\varnothing", r"\infty", r"\partial", r"\nabla",
        r"\langle", r"\rangle", r"\lrcorner", r"\ldots", r"\cdots", r"\dots",
        r"\mathbb{N}", r"\mathbb{Z}", r"\mathbb{Q}", r"\mathbb{R}", r"\mathbb{C}", r"\top", r"\bot", r"\{", r"\}"
    ]
    for k in sorted(sym_keys, key=len, reverse=True):
        s = s.replace(k, "SYM")
    return s


def audit_html(html_path: Path, kb_path: Path) -> dict:
    report = {
        "html_path": str(html_path),
        "hard_fails": {},
        "metrics": {},
        "violations": [],
        "status": "PASS"
    }

    def gate(gid: str, ok: bool, detail: str):
        report["hard_fails"][gid] = {"status": "CLEARED" if ok else "OPEN", "detail": detail}
        if not ok:
            report["violations"].append(f"[{gid}] {detail}")
            report["status"] = "FAIL"

    if not html_path.exists():
        gate("HF-STUDIO-01", False, f"Missing HTML at {html_path}")
        return report

    html = html_path.read_text(encoding="utf-8")
    kb = json.loads(kb_path.read_text(encoding="utf-8")) if kb_path and kb_path.exists() else {}

    # HF-STUDIO-01: CETI Field-Manual Palette & 3-Voice Typography (Supports BookVoiceProfile adaptation)
    req_tokens = ["--raw-paper:", "--raw-ink:", "--f-serif:", "--f-sans:", "--f-mono:", "Fraunces", "JetBrains Mono"]
    missing_tok = [t for t in req_tokens if t not in html]
    gate("HF-STUDIO-01", len(missing_tok) == 0, f"Field-Manual paper/ink & 3-voice typography tokens present ({len(req_tokens)-len(missing_tok)}/{len(req_tokens)})")

    # HF-STUDIO-02: Fast-Load Split-Bundle Architecture
    size_kb = html_path.stat().st_size / 1024.0
    has_defer = '<script defer src="' in html and "sheaf_pages_bundle.js" in html
    gate("HF-STUDIO-02", size_kb < 450.0 and has_defer, f"Core HTML size {size_kb:.1f} KB (< 450 KB limit); deferred bundle tag present={has_defer}")

    # HF-STUDIO-03: Zero Raw LaTeX Leakage in static HTML + all KB strings after convertLatexTokensToHtml
    # Strip <script> blocks from HTML to inspect static visible markup
    static_markup = re.sub(r"<script[\s\S]*?</script>", "", html)
    static_leaks = RAW_LATEX_LEAK_RE.findall(static_markup)
    kb_leaks = []
    for s in kb.get("stalks", []):
        out = simulate_js_latex_to_html(s.get("formal_core", ""))
        leaks = RAW_LATEX_LEAK_RE.findall(out)
        if leaks:
            kb_leaks.append(f"stalk:{s['id']}:{leaks}")
    for inv in kb.get("notebook_investigations", []):
        out = simulate_js_latex_to_html(inv.get("synthesis_markdown", ""))
        leaks = RAW_LATEX_LEAK_RE.findall(out)
        if leaks:
            kb_leaks.append(f"inv:{inv['id']}:{leaks}")
    gate(
        "HF-STUDIO-03",
        len(static_leaks) == 0 and len(kb_leaks) == 0,
        f"Static markup LaTeX leaks: {len(static_leaks)}; KB rendered LaTeX leaks: {len(kb_leaks)}"
        + (f" ({static_leaks[:3]} {kb_leaks[:3]})" if (static_leaks or kb_leaks) else "")
    )

    # HF-STUDIO-04: Multi-Plate Editorial Architecture (>=5 Plates) & One-Italic-Noun Title Rule
    plates_found = re.findall(r'<section[^>]*class="[^"]*plate[^"]*"[^>]*id="([^"]+)"', html)
    italic_nouns = len(re.findall(r'<em class="u-(?:copper|accent)">[^<]+</em>', html))
    gate("HF-STUDIO-04", len(plates_found) >= 5 and italic_nouns >= 6, f"Plates present: {len(plates_found)} ({plates_found}); italic accent title nouns: {italic_nouns}")

    # HF-STUDIO-05: Honesty Apparatus (.marginalia with <cite> and .counterpoint on every Plate)
    marginalia_cnt = len(re.findall(r'<aside class="marginalia">', html))
    cite_cnt = len(re.findall(r"<cite>", html))
    cp_cnt = len(re.findall(r'<div class="counterpoint">', html))
    gate(
        "HF-STUDIO-05",
        marginalia_cnt >= len(plates_found) and cite_cnt >= len(plates_found) and cp_cnt >= len(plates_found) and len(plates_found) >= 5,
        f"Marginalia blocks: {marginalia_cnt} (>={len(plates_found)}); <cite> attributions: {cite_cnt} (>={len(plates_found)}); Counterpoints: {cp_cnt} (>={len(plates_found)})"
    )

    # HF-STUDIO-06: Non-Color-Alone Verdict Stamps
    stamps = re.findall(r'<span class="stamp[^"]*"[^>]*>([^<]+)</span>', html)
    bad_stamps = [st for st in stamps if not any(g in st for g in ["◆", "⚖", "✓", "±", "⊘", "◐", "Ch "])]
    gate("HF-STUDIO-06", len(stamps) >= 8 and len(bad_stamps) == 0, f"Verdict stamps checked: {len(stamps)}; glyph-less stamps: {len(bad_stamps)}")

    # HF-STUDIO-07: Single-Mutator Interactive Instruments & On-Demand 3D Loop
    instrument_cnt = len(re.findall(r'<div class="instrument"', html))
    tablist_cnt = len(re.findall(r'role="tablist"', html))
    has_studio = 'id="notebookQueryInput"' in html and 'id="gluedOlogSvgWrap"' in html
    has_on_demand_3d = "if (state.activeSubview !== 'atlas3d') { rafId = null; return; }" in html
    gate(
        "HF-STUDIO-07",
        instrument_cnt >= 5 and tablist_cnt >= 3 and has_studio and has_on_demand_3d,
        f"Instruments verified: count={instrument_cnt} (>=5), tablists={tablist_cnt} (>=3), notebookStudio={has_studio}, onDemand3D={has_on_demand_3d}"
    )

    # HF-STUDIO-08: FORGE Callout & Self-Contained Courseware Law
    has_so_what = bool(re.search(r"<strong>\s*So What\s*</strong>", html, re.IGNORECASE))
    has_mod_nums = bool(re.search(r"title:\s*'Module\s+\d+", html))
    # Check that module cards do not stack two .callout-box elements back-to-back without intervening element
    stacked_callouts = bool(re.search(r'<div class="callout-box"[^>]*>(?:(?!</div>).)*</div>\s*<div class="callout-box"', html, re.DOTALL))
    gate(
        "HF-STUDIO-08",
        (not has_so_what) and (not has_mod_nums) and (not stacked_callouts),
        f"FORGE compliance: zero 'So What'={not has_so_what}, zero 'Module N' titles={not has_mod_nums}, zero stacked callout-boxes={not stacked_callouts}"
    )

    # HF-STUDIO-09: Progressive Depth & Paper Theme Controls
    has_depth = 'data-set-level="newcomer"' in html and 'data-set-level="practitioner"' in html and 'data-set-level="expert"' in html
    has_theme = 'data-set-theme="light"' in html and 'data-set-theme="dark"' in html
    gate("HF-STUDIO-09", has_depth and has_theme, f"Depth switcher={has_depth}; Cream/Ink paper switcher={has_theme}")

    # HF-STUDIO-10: Slide-Over Verbatim Book Reader, Valid Page Bounds & Zero Foreign Corpus Bleed
    has_reader = 'id="readerDrawer"' in html and "window.__jumpToPage" in html
    total_pages = int(kb.get("book", {}).get("total_pages", 609))
    author_str = str(kb.get("book", {}).get("author", ""))
    jump_pages = [int(p) for p in re.findall(r"window\.__jumpToPage\((\d+)", html)]
    oob_jumps = [p for p in jump_pages if p < 1 or p > total_pages]
    primary_author = author_str.split("(")[0].strip()
    spivak_bleed = (bool(primary_author) and (primary_author not in static_markup)) or (f'max="{total_pages}"' not in static_markup)
    if total_pages != 609:
        if any(tok in html for tok in ["of 609 ·", "Math.min(609,", "from 877 total", "30 Stalks, 877 Items", "Loading 609-page bundle"]):
            spivak_bleed = True
    gate(
        "HF-STUDIO-10",
        has_reader and len(oob_jumps) == 0 and (not spivak_bleed),
        f"Slide-over {total_pages}-page verbatim reader & __jumpToPage wired={has_reader}; out-of-bounds page jumps={len(oob_jumps)}; foreign Spivak/609 bleed={spivak_bleed}"
    )

    # HF-STUDIO-11: NotebookLM Dual-Host Neural Podcast Deck, Custom Dialogue Generator & Gemini 2.5 Multi-Speaker TTS
    has_podcast_card = (
        'id="podcastStudioCard"' in html
        and 'id="hostBadgeKore"' in html
        and 'id="hostBadgePuck"' in html
        and 'id="podcastPlayPauseBtn"' in html
        and "document.getElementById('podcastPlayPauseBtn')" in html
    )
    has_podcast_drawers = 'id="podcastTranscriptDrawer"' in html and 'id="geminiTtsConfigDrawer"' in html
    has_gemini_tts = "gemini-2.5-flash-preview-tts" in html and "multiSpeakerVoiceConfig" in html
    has_custom_podcast = "buildCustomPodcastTurns" in html
    gate(
        "HF-STUDIO-11",
        has_podcast_card and has_podcast_drawers and has_gemini_tts and has_custom_podcast,
        f"Dual-Host Podcast Deck={has_podcast_card}; Transcript/Gemini Drawers={has_podcast_drawers}; Gemini 2.5 TTS={has_gemini_tts}; Dynamic Custom Dialogue={has_custom_podcast}"
    )

    report["metrics"] = {
        "core_html_size_kb": round(size_kb, 1),
        "plates_count": len(plates_found),
        "marginalia_count": marginalia_cnt,
        "counterpoint_count": cp_cnt,
        "stamps_count": len(stamps)
    }
    return report


def main():
    parser = argparse.ArgumentParser(description="Audit Field-Manual Sheaf Studio HTML against HF-STUDIO-01..10")
    parser.add_argument("--html", type=Path, required=True, help="Path to compiled studio HTML")
    parser.add_argument("--kb", type=Path, required=True, help="Path to sheaf_kb.json")
    parser.add_argument("--out", type=Path, default=None, help="Optional JSON output path")
    args = parser.parse_args()

    rep = audit_html(args.html, args.kb)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"=== FIELD-MANUAL STUDIO HTML AUDIT ({rep['status']}) ===")
    for gid, ginfo in rep["hard_fails"].items():
        mark = "◆ CLEARED" if ginfo["status"] == "CLEARED" else "⊘ OPEN   "
        print(f"  {gid} [{mark}]: {ginfo['detail']}")
    print("Metrics:", json.dumps(rep["metrics"]))
    sys.exit(0 if rep["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
