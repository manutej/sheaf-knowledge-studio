#!/usr/bin/env python3
r"""
run_sheaf_pipeline_audit.py
===========================
Executes the complete 4-Evaluator (A1–A4) Adversarial Audit across:
  - `sheaf_kb.json`, `sheaf_pages_bundle.js`, `cattheory_sheaf.db`, and `wiki/` (via `validate_sheaf_contract.py`)
  - Compiled Field-Manual Studio HTML (via `audit_rendered_html.py`)
  - Live CLI & JSON-RPC 2.0 `--mcp` server health check (`query_sheaf.py --mcp`)
  - Master Typed Meta-Prompt Contract (`TYPED-CONTRACT-SHEAF-META-PROMPT.md`) completeness check
Outputs a structured A1–A4 MOE Evaluation JSON + Markdown summary.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
SKILLS_ROOT = THIS_DIR.parents[1]
ROOT = THIS_DIR.parents[3] if (THIS_DIR.parents[3] / ".agents").exists() else THIS_DIR.parents[2]

VALIDATE_SCRIPT = (
    SKILLS_ROOT / "sheaf-corpus-indexer/scripts/validate_sheaf_contract.py"
    if (SKILLS_ROOT / "sheaf-corpus-indexer/scripts/validate_sheaf_contract.py").exists()
    else ROOT / ".agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py"
)
AUDIT_HTML_SCRIPT = (
    SKILLS_ROOT / "sheaf-field-manual-studio/scripts/audit_rendered_html.py"
    if (SKILLS_ROOT / "sheaf-field-manual-studio/scripts/audit_rendered_html.py").exists()
    else ROOT / ".agents/skills/sheaf-field-manual-studio/scripts/audit_rendered_html.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_mcp_server(query_script: Path) -> tuple[bool, str]:
    if not query_script.exists():
        return False, f"Missing {query_script}"
    req = '{"jsonrpc":"2.0","id":1,"method":"tools/list"}\n'
    try:
        proc = subprocess.run(
            [sys.executable, str(query_script), "--mcp"],
            input=req,
            text=True,
            capture_output=True,
            timeout=8
        )
        out = proc.stdout.strip()
        data = json.loads(out.splitlines()[0])
        tools = [t["name"] for t in data.get("result", {}).get("tools", [])]
        ok = {"sheaf_query", "sheaf_inspect_stalk", "sheaf_read_page"}.issubset(set(tools))
        return ok, f"MCP stdio server tools verified: {tools}"
    except Exception as e:
        return False, f"MCP stdio check failed: {e}"


def main():
    parser = argparse.ArgumentParser(description="Run full A1-A4 MOE Adversarial Audit on a Sheaf Knowledge Base & Studio")
    parser.add_argument("--kb", type=Path, default=ROOT / "cattheory-sheaf-kb/data/sheaf_kb.json")
    parser.add_argument("--html", type=Path, default=ROOT / "Category Theory Sheaf Knowledge Base - Notebook Studio.html")
    parser.add_argument("--query-script", type=Path, default=ROOT / "cattheory-sheaf-kb/query_sheaf.py")
    parser.add_argument("--contract-doc", type=Path, default=ROOT / "cattheory-sheaf-kb/TYPED-CONTRACT-SHEAF-META-PROMPT.md")
    parser.add_argument("--out", type=Path, default=ROOT / "cattheory-sheaf-kb/adversarial-eval/latest_moe_audit.json")
    args = parser.parse_args()

    val_mod = load_module("validate_sheaf_contract", VALIDATE_SCRIPT)
    aud_mod = load_module("audit_rendered_html", AUDIT_HTML_SCRIPT)

    sheaf_res = val_mod.check_sheaf_contract(args.kb)
    html_res = aud_mod.audit_html(args.html, args.kb)
    mcp_ok, mcp_detail = test_mcp_server(args.query_script)

    contract_ok = args.contract_doc.exists() and args.contract_doc.stat().st_size > 8000
    contract_detail = (
        f"Typed Meta-Prompt Contract present ({args.contract_doc.stat().st_size / 1024:.1f} KB)"
        if contract_ok else f"Missing or thin contract doc at {args.contract_doc}"
    )

    all_gates = {}
    all_gates.update(sheaf_res["hard_fails"])
    all_gates.update(html_res["hard_fails"])
    all_gates["HF-MCP-01"] = {"status": "CLEARED" if mcp_ok else "OPEN", "detail": mcp_detail}
    all_gates["HF-CONTRACT-01"] = {"status": "CLEARED" if contract_ok else "OPEN", "detail": contract_detail}

    a1_ids = ["HF-SHEAF-01", "HF-SHEAF-02", "HF-SHEAF-03", "HF-SHEAF-04", "HF-SHEAF-05", "HF-SHEAF-06", "HF-SHEAF-07", "HF-STUDIO-07"]
    a2_ids = ["HF-SHEAF-10", "HF-SHEAF-11", "HF-STUDIO-02", "HF-STUDIO-09", "HF-MCP-01", "HF-CONTRACT-01"]
    a3_ids = ["HF-STUDIO-01", "HF-STUDIO-03", "HF-STUDIO-04", "HF-STUDIO-05", "HF-STUDIO-06", "HF-STUDIO-08", "HF-STUDIO-11", "HF-STUDIO-12"]
    a4_ids = ["HF-SHEAF-08", "HF-SHEAF-09", "HF-SHEAF-12", "HF-SHEAF-13", "HF-STUDIO-10"]

    def lens_summary(ids):
        open_g = [i for i in ids if all_gates.get(i, {}).get("status") != "CLEARED"]
        return {
            "vote": "GO" if not open_g else "NO-GO",
            "cleared_count": len(ids) - len(open_g),
            "total_count": len(ids),
            "open_gates": open_g,
            "gates": {i: all_gates.get(i) for i in ids}
        }

    moe = {
        "overall_ship_vote": "GO" if all(g["status"] == "CLEARED" for g in all_gates.values()) else "NO-GO",
        "total_gates_cleared": sum(1 for g in all_gates.values() if g["status"] == "CLEARED"),
        "total_gates": len(all_gates),
        "evaluators": {
            "A1_Depth_Olog_Cohomology": lens_summary(a1_ids),
            "A2_Performance_FTS5_MCP_Contract": lens_summary(a2_ids),
            "A3_FieldManual_Math_SymbolicCraft": lens_summary(a3_ids),
            "A4_Citations_PageFibers_Wiki": lens_summary(a4_ids)
        },
        "sheaf_metrics": sheaf_res["metrics"],
        "studio_metrics": html_res["metrics"]
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(moe, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"=== MOE ADVERSARIAL PIPELINE AUDIT: {moe['overall_ship_vote']} ({moe['total_gates_cleared']}/{moe['total_gates']} GATES CLEARED) ===")
    for agent_name, info in moe["evaluators"].items():
        print(f"  [{info['vote']}] {agent_name}: {info['cleared_count']}/{info['total_count']} cleared" + (f" (OPEN: {info['open_gates']})" if info["open_gates"] else ""))
    sys.exit(0 if moe["overall_ship_vote"] == "GO" else 1)


if __name__ == "__main__":
    main()
