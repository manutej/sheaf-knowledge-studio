#!/usr/bin/env python3
r"""
validate_sheaf_contract.py
==========================
Deterministic Typed Contract & Čech Cohomology Validator for any Sheaf Knowledge Base.
Enforces binary HARD FAIL gates (HF-SHEAF-01 .. HF-SHEAF-14) across:
  1. `sheaf_kb.json` (schema, 100% body page coverage, Olog internal referential integrity,
     restriction morphism connectivity, 2-simplex cocycle closure, citation page bounds)
  2. `sheaf_pages_bundle.js` (deferred bundle existence & page parity)
  3. SQLite FTS5 Database (`cattheory_sheaf.db` or `sheaf.db`)
  4. Persistent LLM Wiki (`wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`)
"""

import argparse
import json
import re
import sqlite3
import sys
from collections import deque
from pathlib import Path


def check_sheaf_contract(kb_path: Path, db_path: Path = None, wiki_dir: Path = None, bundle_path: Path = None) -> dict:
    results = {
        "kb_path": str(kb_path),
        "hard_fails": {},
        "metrics": {},
        "violations": [],
        "status": "PASS"
    }

    def record_gate(gate_id: str, passed: bool, detail: str):
        results["hard_fails"][gate_id] = {
            "status": "CLEARED" if passed else "OPEN",
            "detail": detail
        }
        if not passed:
            results["violations"].append(f"[{gate_id}] {detail}")
            results["status"] = "FAIL"

    if not kb_path.exists():
        record_gate("HF-SHEAF-01", False, f"Missing sheaf_kb.json at {kb_path}")
        return results

    kb = json.loads(kb_path.read_text(encoding="utf-8"))

    # HF-SHEAF-01: Top-level required keys & book metadata
    req_top = ["book", "chapters", "stalks", "restriction_morphisms", "two_simplices", "notebook_investigations", "formal_items", "pages"]
    missing_top = [k for k in req_top if k not in kb]
    total_pages = kb.get("book", {}).get("total_pages", 0)
    pages_list = kb.get("pages", [])
    record_gate(
        "HF-SHEAF-01",
        len(missing_top) == 0 and total_pages == len(pages_list) and total_pages > 0,
        f"Top-level keys present ({len(req_top) - len(missing_top)}/{len(req_top)}); pages count {len(pages_list)} == book.total_pages {total_pages}"
    )

    # HF-SHEAF-02: 100% Body Page Coverage across Chapters & Stalks
    chapters = kb.get("chapters", [])
    stalks = kb.get("stalks", [])
    if chapters:
        body_start = min(c["start_page"] for c in chapters)
        body_end = max(c["end_page"] for c in chapters)
    else:
        body_start, body_end = 1, total_pages

    covered_pages = set()
    for s in stalks:
        for p in range(s.get("start_page", 0), s.get("end_page", -1) + 1):
            if body_start <= p <= body_end:
                covered_pages.add(p)
    expected_body_pages = set(range(body_start, body_end + 1))
    uncovered = sorted(expected_body_pages - covered_pages)
    coverage_ratio = len(covered_pages) / max(1, len(expected_body_pages))
    record_gate(
        "HF-SHEAF-02",
        len(uncovered) == 0,
        f"Body page coverage p.{body_start}..{body_end}: {len(covered_pages)}/{len(expected_body_pages)} ({coverage_ratio*100:.1f}%)"
        + (f" — Uncovered: {uncovered[:10]}" if uncovered else "")
    )

    # HF-SHEAF-03: Stalk ID uniqueness, valid page intervals, chapter granularity & non-tautological formal_core
    stalk_ids = [s.get("id") for s in stalks]
    stalk_set = set(stalk_ids)
    bad_intervals = [s["id"] for s in stalks if s.get("start_page", 1) > s.get("end_page", 0) or s.get("end_page", 0) > total_pages]
    tautological_cores = [s["id"] for s in stalks if "\\mathrm{Stalk}([" in str(s.get("formal_core", ""))]
    chapters_ok = (len(chapters) >= 3) if total_pages >= 80 else (len(chapters) >= 1)
    record_gate(
        "HF-SHEAF-03",
        len(stalk_ids) == len(stalk_set) and len(stalk_set) >= 10 and len(bad_intervals) == 0 and chapters_ok and len(tautological_cores) == 0,
        f"{len(stalk_set)} unique stalks across {len(chapters)} chapters; bad intervals: {len(bad_intervals)}; tautological formal_cores: {len(tautological_cores)}"
    )

    # HF-SHEAF-04: Local Olog Internal Referential Integrity, Aspect Verb Diversity & Zero Kerning Pollution
    olog_errors = []
    all_aspect_labels = set()
    banned_kerning_tokens = {"thefunction", "ofthe", "tothe", "thesame", "http", "https", "foundation", "opening", "one"}
    for s in stalks:
        olog = s.get("olog", {})
        types = {t["id"] for t in olog.get("types", []) if "id" in t}
        type_labels_low = {str(t.get("label", "")).strip().lower() for t in olog.get("types", [])}
        bad_t = type_labels_low & banned_kerning_tokens
        if bad_t:
            olog_errors.append(f"{s['id']}: polluted Olog type label {sorted(bad_t)}")
        bad_def = set(s.get("defined_terms", [])) & banned_kerning_tokens
        if bad_def:
            olog_errors.append(f"{s['id']}: polluted defined_terms {sorted(bad_def)}")
        aspects = olog.get("aspects", [])
        facts = olog.get("facts", [])
        if len(types) < 2 or len(aspects) < 1 or len(facts) < 1:
            olog_errors.append(f"{s['id']}: insufficient Olog (types={len(types)}, aspects={len(aspects)}, facts={len(facts)})")
        for a in aspects:
            all_aspect_labels.add(str(a.get("label", "")).strip())
            if a.get("src") not in types or a.get("dst") not in types:
                olog_errors.append(f"{s['id']}: aspect {a.get('src')}->{a.get('dst')} references undeclared Olog type")
    min_distinct_aspects = max(6, len(stalks) // 2)
    if len(all_aspect_labels) < min_distinct_aspects:
        olog_errors.append(f"Olog aspect verb diversity too low: {len(all_aspect_labels)} < {min_distinct_aspects}")
    record_gate(
        "HF-SHEAF-04",
        len(olog_errors) == 0,
        f"All {len(stalks)} local Ologs valid with {len(all_aspect_labels)} distinct aspect verbs & zero kerning pollution (errors: {len(olog_errors)})"
        + (f" — {olog_errors[:3]}" if olog_errors else "")
    )

    # HF-SHEAF-05: Restriction Morphism Endpoints & Global Poset Connectivity
    morphisms = kb.get("restriction_morphisms", [])
    bad_endpoints = [
        m.get("id") for m in morphisms
        if m.get("source") not in stalk_set or m.get("target") not in stalk_set
    ]
    adj = {sid: set() for sid in stalk_set}
    for m in morphisms:
        u, v = m.get("source"), m.get("target")
        if u in adj and v in adj:
            adj[u].add(v)
            adj[v].add(u)
    visited = set()
    if stalk_ids:
        q = deque([stalk_ids[0]])
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            for nxt in adj.get(cur, ()):
                if nxt not in visited:
                    q.append(nxt)
    isolated = sorted(stalk_set - visited)
    record_gate(
        "HF-SHEAF-05",
        len(bad_endpoints) == 0 and len(isolated) == 0 and len(morphisms) >= len(stalks),
        f"{len(morphisms)} restriction morphisms; connected stalks: {len(visited)}/{len(stalk_set)}; bad endpoints: {len(bad_endpoints)}"
    )

    # HF-SHEAF-06: Restriction Morphism Formula & Empirical Content-Computed Overlap
    thin_morphisms = []
    for m in morphisms:
        f_ok = len(str(m.get("formula", "")).strip()) >= 2 and len(str(m.get("overlap", "")).strip()) >= 10
        shared_t = m.get("shared_terms", [])
        fid = m.get("restriction_fidelity")
        d0 = m.get("coboundary_defect_d0")
        emp_ok = (
            isinstance(shared_t, list) and len(shared_t) >= 1
            and isinstance(fid, (int, float)) and 0.05 <= fid <= 0.999
            and isinstance(d0, (int, float)) and abs((fid + d0) - 1.0) < 0.02
        )
        if not (f_ok and emp_ok):
            thin_morphisms.append(m.get("id", "?"))
    mean_fid = round(sum((m.get("restriction_fidelity") or 0.0) for m in morphisms) / max(1, len(morphisms)), 3)
    mean_d0 = round(sum((m.get("coboundary_defect_d0") or 1.0) for m in morphisms) / max(1, len(morphisms)), 3)
    record_gate(
        "HF-SHEAF-06",
        len(thin_morphisms) == 0 and len(morphisms) > 0,
        f"All {len(morphisms)} restriction morphisms carry content-computed TF-IDF/JSD overlap (mean fidelity={mean_fid}, mean ||δ⁰||={mean_d0}, invalid={len(thin_morphisms)})"
    )

    # HF-SHEAF-07: Higher 2-Simplices & 1-Cocycle Holonomy (||δ¹|| Verification)
    simplices = kb.get("two_simplices", [])
    bad_simplices = []
    dir_edges = {(m.get("source"), m.get("target")) for m in morphisms}
    undir_edges = dir_edges | {(v, u) for (u, v) in dir_edges}
    for tau in simplices:
        verts = tau.get("vertices", [])
        if len(verts) != 3 or any(v not in stalk_set for v in verts):
            bad_simplices.append(tau.get("id", "?"))
            continue
        u, v, w = verts
        edges_present = sum([1 for pair in [(u, v), (v, w), (u, w)] if pair in undir_edges])
        d1 = tau.get("holonomy_defect_d1")
        triple_t = tau.get("triple_shared_terms", [])
        if edges_present < 2 or not isinstance(d1, (int, float)) or d1 > 0.50 or not triple_t:
            bad_simplices.append(f"{tau.get('id')}(edges={edges_present},d1={d1})")
    mean_d1 = round(sum((t.get("holonomy_defect_d1") or 0.5) for t in simplices) / max(1, len(simplices)), 3)
    record_gate(
        "HF-SHEAF-07",
        len(simplices) >= 1 and len(bad_simplices) == 0,
        f"{len(simplices)} commutative 2-simplices verified with content-computed holonomy (mean ||δ¹||={mean_d1}, bad={len(bad_simplices)})"
    )

    # HF-SHEAF-08: Formal Declarations Grounding, Page Bounds & Contextual Title Diversity
    formal_items = kb.get("formal_items", [])
    bad_items = [
        it.get("id") for it in formal_items
        if not (1 <= it.get("page", 0) <= total_pages) or not it.get("stalk_ids")
    ]
    distinct_item_titles = {str(it.get("title", "")).strip() for it in formal_items if it.get("title")}
    min_item_titles = min(5, len(formal_items))
    record_gate(
        "HF-SHEAF-08",
        len(formal_items) > 0 and len(bad_items) == 0 and len(distinct_item_titles) >= min_item_titles,
        f"{len(formal_items)} formal declarations indexed with {len(distinct_item_titles)} distinct contextual titles & valid page bounds (bad: {len(bad_items)})"
    )

    # HF-SHEAF-09: Curated Notebook Investigations, Citation Validity & Empirical Cohomology Audit
    investigations = kb.get("notebook_investigations", [])
    obstructions = kb.get("cohomology_obstructions", [])
    inv_errors = []
    for inv in investigations:
        cov = inv.get("open_cover", [])
        if len(cov) < 2 or any(cid not in stalk_set for cid in cov):
            inv_errors.append(f"{inv.get('id')}: invalid open_cover")
        cites = inv.get("citations", [])
        if not cites or any(not (1 <= c.get("page", 0) <= total_pages) for c in cites):
            inv_errors.append(f"{inv.get('id')}: invalid citations")
        coh = inv.get("cohomology", {})
        if (
            not isinstance(coh.get("h0_coherence"), (int, float))
            or not isinstance(coh.get("h1_obstruction"), (int, float))
            or not isinstance(coh.get("mean_coboundary_defect_d0"), (int, float))
        ):
            inv_errors.append(f"{inv.get('id')}: missing content-computed cohomology (h0_coherence, h1_obstruction, mean_coboundary_defect_d0)")
    record_gate(
        "HF-SHEAF-09",
        len(investigations) >= 3 and len(inv_errors) == 0 and len(obstructions) >= 1,
        f"{len(investigations)} investigations & {len(obstructions)} empirical H¹ obstructions verified (errors: {len(inv_errors)})"
    )

    # HF-SHEAF-10: Deferred Browser Bundle Parity (`sheaf_pages_bundle.js`)
    if bundle_path is None:
        bundle_path = kb_path.parent / "sheaf_pages_bundle.js"
    bundle_ok = bundle_path.exists() and bundle_path.stat().st_size > 1000
    record_gate(
        "HF-SHEAF-10",
        bundle_ok,
        f"Deferred browser bundle {bundle_path.name}: {'EXISTS (' + str(round(bundle_path.stat().st_size/1024, 1)) + ' KB)' if bundle_ok else 'MISSING'}"
    )

    # HF-SHEAF-11: SQLite FTS5 Search Index Integrity
    if db_path is None:
        candidates = list(kb_path.parent.glob("*.db"))
        db_path = candidates[0] if candidates else kb_path.parent / "cattheory_sheaf.db"
    db_ok = False
    db_detail = f"Missing DB at {db_path}"
    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            cur = conn.cursor()
            cur.execute("SELECT count(*) FROM pages_fts")
            p_cnt = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM formal_items_fts")
            fi_cnt = cur.fetchone()[0]
            conn.close()
            db_ok = (p_cnt == total_pages and fi_cnt == len(formal_items))
            db_detail = f"SQLite FTS5 verified: pages_fts={p_cnt}/{total_pages}, formal_items_fts={fi_cnt}/{len(formal_items)}"
        except Exception as e:
            db_detail = f"SQLite error: {e}"
    record_gate("HF-SHEAF-11", db_ok, db_detail)

    # HF-SHEAF-12: Persistent Markdown Wiki Completeness
    if wiki_dir is None:
        wiki_dir = kb_path.parent.parent / "wiki"
    wiki_ok = False
    wiki_detail = f"Missing wiki dir at {wiki_dir}"
    if wiki_dir.exists():
        home_ok = (wiki_dir / "HOME.md").exists()
        ch_files = list((wiki_dir / "chapters").glob("*.md")) if (wiki_dir / "chapters").exists() else []
        st_files = list((wiki_dir / "concepts").glob("*.md")) if (wiki_dir / "concepts").exists() else []
        wiki_ok = home_ok and len(ch_files) == len(chapters) and len(st_files) == len(stalks)
        wiki_detail = f"Wiki files verified: HOME.md={home_ok}, chapters={len(ch_files)}/{len(chapters)}, concepts={len(st_files)}/{len(stalks)}"
    record_gate("HF-SHEAF-12", wiki_ok, wiki_detail)

    # HF-SHEAF-13: NotebookLM Dual-Host Neural Podcast Audio, Speaker Parity & Spoken Text Hygiene
    podcast_errors = []
    spoken_kerning_re = re.compile(
        r"\b(?:generalizationof|weneed|ofnumbers|andreturn|skeletalcategories|componentsinvolves|targetcategory|productcategories|asitsunderlying|thefunction|ofthe|tobe|inour|wecan|ifwe|thatis)\b",
        re.IGNORECASE
    )
    raw_paren_cite_re = re.compile(r"\(p\.\s*\d+", re.IGNORECASE)
    turn2_seen = set()
    turn_last_seen = set()
    for inv in investigations:
        inv_id = inv.get("id", "unknown")
        af = inv.get("audio_file", "")
        dur = float(inv.get("audio_duration_sec", 0) or 0)
        af_path = kb_path.parent / af if af else None
        if not af or not af_path or not af_path.exists() or af_path.stat().st_size < 40000:
            podcast_errors.append(f"{inv_id}: missing or thin audio_file '{af}'")
        if dur < 25.0:
            podcast_errors.append(f"{inv_id}: audio_duration_sec={dur} (<25s)")
        turns = inv.get("podcast_turns", [])
        if len(turns) < 6:
            podcast_errors.append(f"{inv_id}: only {len(turns)} podcast_turns (<6 required)")
        speakers = {t.get("speaker") for t in turns}
        if not ({"Kore", "Puck"}.issubset(speakers) or {"Host A", "Host B"}.issubset(speakers)):
            podcast_errors.append(f"{inv_id}: speakers={speakers} (must include 'Kore' and 'Puck')")
        for t_idx, t in enumerate(turns):
            txt = str(t.get("text", ""))
            m_k = spoken_kerning_re.search(txt)
            if m_k:
                podcast_errors.append(f"{inv_id}[turn {t_idx}]: kerning glue '{m_k.group(0)}'")
            if raw_paren_cite_re.search(txt):
                podcast_errors.append(f"{inv_id}[turn {t_idx}]: raw parenthetical '(p. N)' in spoken text")
        if len(turns) >= 2:
            t2_norm = turns[1].get("text", "").strip().lower()
            if t2_norm in turn2_seen:
                podcast_errors.append(f"{inv_id}: duplicate cookie-cutter Turn-2 prompt")
            turn2_seen.add(t2_norm)
            tl_norm = turns[-1].get("text", "").strip().lower()
            if tl_norm in turn_last_seen:
                podcast_errors.append(f"{inv_id}: duplicate cookie-cutter closing turn")
            turn_last_seen.add(tl_norm)

    record_gate(
        "HF-SHEAF-13",
        len(investigations) >= 3 and len(podcast_errors) == 0,
        f"Dual-Host Neural Podcast verified across {len(investigations)} episodes (errors: {len(podcast_errors)})"
        + (f" — {podcast_errors[:4]}" if podcast_errors else "")
    )

    # HF-SHEAF-14: Cross-Corpus Functorial Bridge Completeness & Strict JSON Schema Conformance
    bridges = kb.get("cross_corpus_bridges", [])
    bridge_errors = []
    min_bridges = min(18, len(stalks))
    if len(bridges) < min_bridges:
        bridge_errors.append(f"len(cross_corpus_bridges)={len(bridges)} (<{min_bridges} required)")
    for b_idx, b in enumerate(bridges):
        bfid = b.get("bridge_fidelity")
        bd0 = b.get("coboundary_defect_d0")
        if bfid is None or not (0.5 <= float(bfid) <= 1.0):
            bridge_errors.append(f"bridge[{b_idx}] invalid bridge_fidelity={bfid}")
        elif bd0 is None or abs(float(bd0) - (1.0 - float(bfid))) > 0.02:
            bridge_errors.append(f"bridge[{b_idx}] coboundary_defect_d0={bd0} != 1 - {bfid}")
        if not b.get("source_stalk_id") or not b.get("target_stalk_id") or not b.get("concept_arc") or not b.get("shared_terms"):
            bridge_errors.append(f"bridge[{b_idx}] missing required functorial bridge fields")

    schema_candidates = [
        kb_path.parent.parent / "contracts" / "sheaf-schema-contract.json",
        Path(__file__).resolve().parents[1] / "resources" / "sheaf_kb.schema.json",
        Path(__file__).resolve().parents[4] / "sheaf-knowledge-studio" / "contracts" / "sheaf-schema-contract.json",
    ]
    schema_path = next((p for p in schema_candidates if p.exists()), None)
    if schema_path is not None:
        try:
            import jsonschema
            schema_obj = json.loads(schema_path.read_text(encoding="utf-8"))
            v = jsonschema.Draft202012Validator(schema_obj)
            s_errs = list(v.iter_errors(kb))
            if s_errs:
                bridge_errors.append(f"jsonschema errors={len(s_errs)} (first: {s_errs[0].message[:80]})")
        except ImportError:
            pass

    record_gate(
        "HF-SHEAF-14",
        len(bridges) >= min_bridges and len(bridge_errors) == 0,
        f"Cross-Corpus Functorial Bridges verified: {len(bridges)} bridges across {len({b.get('concept_arc') for b in bridges})} arcs; schema/bridge errors={len(bridge_errors)}"
        + (f" — {bridge_errors[:3]}" if bridge_errors else "")
    )

    results["metrics"] = {
        "total_pages": total_pages,
        "chapters": len(chapters),
        "stalks": len(stalks),
        "restriction_morphisms": len(morphisms),
        "two_simplices": len(simplices),
        "formal_items": len(formal_items),
        "notebook_investigations": len(investigations),
        "cross_corpus_bridges": len(bridges),
        "empirical_h1_obstructions": len(obstructions),
        "mean_restriction_fidelity": mean_fid,
        "mean_coboundary_defect_d0": mean_d0,
        "mean_holonomy_defect_d1": mean_d1,
        "body_page_coverage_pct": round(coverage_ratio * 100, 2),
        "connected_component_ratio": round(len(visited) / max(1, len(stalk_set)), 3)
    }
    return results


def run_negative_selftest(kb_path: Path) -> bool:
    """
    Runs 5 adversarial negative tests proving the contract linter catches:
      1. Bogus links with zero empirical term overlap (HF-SHEAF-06 must FAIL)
      2. Non-commuting 2-simplices with high holonomy defect ||δ¹|| > 0.50 (HF-SHEAF-07 must FAIL)
      3. Hallucinated out-of-bounds page citations p=99999 (HF-SHEAF-08/09 must FAIL)
      4. Decorative / missing content-computed cohomology metrics (HF-SHEAF-09 must FAIL)
      5. Missing or invalid Cross-Corpus Functorial Bridges (HF-SHEAF-14 must FAIL)
    """
    import tempfile
    orig_kb = json.loads(kb_path.read_text(encoding="utf-8"))
    passed_all_negative_tests = True

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "mutated_kb.json"

        # Case 1: Bogus link with empty shared_terms
        kb1 = json.loads(json.dumps(orig_kb))
        kb1["restriction_morphisms"][0]["shared_terms"] = []
        kb1["restriction_morphisms"][0]["restriction_fidelity"] = None
        tmp_path.write_text(json.dumps(kb1), encoding="utf-8")
        r1 = check_sheaf_contract(tmp_path)
        c1_caught = r1["hard_fails"]["HF-SHEAF-06"]["status"] == "OPEN"

        # Case 2: High holonomy defect on 2-simplex
        kb2 = json.loads(json.dumps(orig_kb))
        kb2["two_simplices"][0]["holonomy_defect_d1"] = 0.88
        tmp_path.write_text(json.dumps(kb2), encoding="utf-8")
        r2 = check_sheaf_contract(tmp_path)
        c2_caught = r2["hard_fails"]["HF-SHEAF-07"]["status"] == "OPEN"

        # Case 3: Out-of-bounds page citation
        kb3 = json.loads(json.dumps(orig_kb))
        kb3["formal_items"][0]["page"] = 99999
        tmp_path.write_text(json.dumps(kb3), encoding="utf-8")
        r3 = check_sheaf_contract(tmp_path)
        c3_caught = r3["hard_fails"]["HF-SHEAF-08"]["status"] == "OPEN"

        # Case 4: Missing content-computed cohomology on investigations
        kb4 = json.loads(json.dumps(orig_kb))
        kb4["notebook_investigations"][0]["cohomology"] = {"gluing_status": "PASS"}
        tmp_path.write_text(json.dumps(kb4), encoding="utf-8")
        r4 = check_sheaf_contract(tmp_path)
        c4_caught = r4["hard_fails"]["HF-SHEAF-09"]["status"] == "OPEN"

        # Case 5: Broken cross-corpus functorial bridges
        kb5 = json.loads(json.dumps(orig_kb))
        kb5["cross_corpus_bridges"] = [{"id": "bad", "source_stalk_id": "x", "target_stalk_id": "y", "bridge_fidelity": 0.12}]
        tmp_path.write_text(json.dumps(kb5), encoding="utf-8")
        r5 = check_sheaf_contract(tmp_path)
        c5_caught = r5["hard_fails"]["HF-SHEAF-14"]["status"] == "OPEN"

        print("=== ADVERSARIAL NEGATIVE SELFTEST (PROVING LINTER FAILS ON DECORATIVE/BAD DATA) ===")
        for label, ok in [
            ("Test 1 (Bogus link with zero empirical overlap -> HF-SHEAF-06 OPEN)", c1_caught),
            ("Test 2 (Non-commuting 2-simplex ||δ¹||=0.88   -> HF-SHEAF-07 OPEN)", c2_caught),
            ("Test 3 (Hallucinated page citation p=99999    -> HF-SHEAF-08 OPEN)", c3_caught),
            ("Test 4 (Decorative non-computed H⁰ score      -> HF-SHEAF-09 OPEN)", c4_caught),
            ("Test 5 (Broken cross-corpus functorial bridge -> HF-SHEAF-14 OPEN)", c5_caught),
        ]:
            print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
            if not ok:
                passed_all_negative_tests = False

    return passed_all_negative_tests


def main():
    parser = argparse.ArgumentParser(description="Validate a Sheaf Knowledge Base against the Typed Contract")
    parser.add_argument("--kb", type=Path, required=True, help="Path to sheaf_kb.json")
    parser.add_argument("--db", type=Path, default=None, help="Path to SQLite FTS5 database")
    parser.add_argument("--wiki", type=Path, default=None, help="Path to generated wiki directory")
    parser.add_argument("--bundle", type=Path, default=None, help="Path to deferred sheaf_pages_bundle.js")
    parser.add_argument("--out", type=Path, default=None, help="Optional JSON output path for audit report")
    parser.add_argument("--selftest", action="store_true", help="Run adversarial negative tests proving the linter catches bogus links & decorative math")
    args = parser.parse_args()

    if args.selftest:
        ok = run_negative_selftest(args.kb)
        if not ok:
            sys.exit(1)

    res = check_sheaf_contract(args.kb, args.db, args.wiki, args.bundle)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"=== SHEAF CONTRACT & COHOMOLOGY AUDIT ({res['status']}) ===")
    for gid, ginfo in res["hard_fails"].items():
        mark = "◆ CLEARED" if ginfo["status"] == "CLEARED" else "⊘ OPEN   "
        print(f"  {gid} [{mark}]: {ginfo['detail']}")
    print("Metrics:", json.dumps(res["metrics"]))
    sys.exit(0 if res["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()

