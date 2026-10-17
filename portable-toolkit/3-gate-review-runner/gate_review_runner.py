#!/usr/bin/env python3
r"""
gate_review_runner.py
=====================
Deterministic Gate-by-Gate Pass/Fail Review Runner & Append-Only Meta-Learning Log.

Designed to be run by builder/evaluator agents at the end of every iteration round:
  1. Executes the fixed list of binary pass/fail gates (Corpus Schema, Page Coverage,
     Citation Bounds, FTS5 Parity, Empirical Overlap, Studio Rendering, MCP Health).
  2. Outputs a structured JSON scorecard (`round_N_scorecard.json`).
  3. Appends a compact, human-and-agent-readable row + open-gate diff to an append-only
     `META-LEARNING-LOG.md` so each round compounds on disk.

Usage:
  python3 gate_review_runner.py --kb path/to/sheaf_kb.json --html path/to/studio.html --round 1 --log-md path/to/META-LEARNING-LOG.md
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIPELINE_AUDIT = ROOT / ".agents/skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py"
VALIDATE_CONTRACT = ROOT / ".agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py"
AUDIT_HTML = ROOT / ".agents/skills/sheaf-field-manual-studio/scripts/audit_rendered_html.py"


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    parser = argparse.ArgumentParser(description="Gate-by-Gate Review Runner for Agent Meta-Learning Logs")
    parser.add_argument("--kb", type=Path, required=True, help="Path to sheaf_kb.json")
    parser.add_argument("--html", type=Path, default=None, help="Optional path to compiled Studio HTML")
    parser.add_argument("--round", type=int, default=1, help="Iteration round number (1, 2, 3...)")
    parser.add_argument("--label", type=str, default="corpus-eval", help="Short label for the run")
    parser.add_argument("--out-json", type=Path, default=None, help="Output JSON scorecard path")
    parser.add_argument("--log-md", type=Path, default=ROOT / "portable-toolkit/META-LEARNING-LOG.md", help="Append-only Markdown meta-learning log")
    args = parser.parse_args()

    val_mod = load_mod("validate_sheaf_contract", VALIDATE_CONTRACT)
    sheaf_res = val_mod.check_sheaf_contract(args.kb)

    gates = dict(sheaf_res["hard_fails"])
    if args.html and args.html.exists():
        aud_mod = load_mod("audit_rendered_html", AUDIT_HTML)
        html_res = aud_mod.audit_html(args.html, args.kb)
        gates.update(html_res["hard_fails"])

    cleared = [gid for gid, g in gates.items() if g["status"] == "CLEARED"]
    open_gates = [gid for gid, g in gates.items() if g["status"] != "CLEARED"]
    verdict = "GO" if not open_gates else "NO-GO"
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    scorecard = {
        "timestamp": ts,
        "round": args.round,
        "label": args.label,
        "verdict": verdict,
        "cleared_count": len(cleared),
        "total_gates": len(gates),
        "open_gates": open_gates,
        "gates": gates,
        "metrics": sheaf_res.get("metrics", {})
    }

    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(scorecard, indent=2, ensure_ascii=False), encoding="utf-8")

    # Append to META-LEARNING-LOG.md
    args.log_md.parent.mkdir(parents=True, exist_ok=True)
    if not args.log_md.exists():
        header = (
            "# Agent Meta-Learning Gate Review Log (Append-Only)\n\n"
            "| Timestamp (UTC) | Round | Corpus / Label | Verdict | Gates Cleared | Open Gates | Key Metrics |\n"
            "|---|---|---|---|---|---|---|\n"
        )
        args.log_md.write_text(header, encoding="utf-8")

    m = sheaf_res.get("metrics", {})
    metrics_str = (
        f"pages={m.get('total_pages')}, items={m.get('formal_items')}, "
        f"fidelity={m.get('mean_restriction_fidelity')}, ||δ⁰||={m.get('mean_coboundary_defect_d0')}"
    )
    open_str = ", ".join(open_gates) if open_gates else "NONE (ALL CLEARED)"
    row = f"| `{ts}` | **R{args.round}** | `{args.label}` | **{verdict}** | `{len(cleared)}/{len(gates)}` | `{open_str}` | {metrics_str} |\n"
    with args.log_md.open("a", encoding="utf-8") as f:
        f.write(row)

    print(f"=== GATE-BY-GATE REVIEW [R{args.round} · {args.label}]: {verdict} ({len(cleared)}/{len(gates)} CLEARED) ===")
    for gid, g in gates.items():
        mark = "PASS" if g["status"] == "CLEARED" else "FAIL"
        print(f"  [{mark}] {gid}: {g['detail']}")
    print(f"Appended round entry to {args.log_md}")
    sys.exit(0 if verdict == "GO" else 1)


if __name__ == "__main__":
    main()
