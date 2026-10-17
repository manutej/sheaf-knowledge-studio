#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "================================================================================"
echo "  CETI SHEAF KNOWLEDGE STUDIO — 27-GATE & NEGATIVE SELFTEST VERIFICATION SUITE"
echo "================================================================================"

echo ""
echo "[1/3] Auditing Build 1: Spivak — Category Theory for the Sciences (609 pp.)"
python3 "skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py" \
  --kb "corpora/spivak-609pp/data/sheaf_kb.json" \
  --html "studios/spivak-category-theory-for-the-sciences/index.html" \
  --query-script "corpora/spivak-609pp/query_sheaf.py" \
  --out "audits/spivak_r3_moe_audit.json"
python3 "skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py" \
  --kb "corpora/spivak-609pp/data/sheaf_kb.json" --selftest >/dev/null
echo "  ✓ Spivak 4/4 Negative Mutation Self-Tests: PASS"

echo ""
echo "[2/3] Auditing Build 2: Marinov — Category Theory Illustrated (Curated 377 pp.)"
python3 "skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py" \
  --kb "corpora/marinov-377pp/data/sheaf_kb.json" \
  --html "studios/marinov-category-theory-illustrated/index.html" \
  --query-script "corpora/marinov-377pp/query_sheaf.py" \
  --out "audits/marinov_r3_moe_audit.json"
python3 "skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py" \
  --kb "corpora/marinov-377pp/data/sheaf_kb.json" --selftest >/dev/null
echo "  ✓ Marinov 4/4 Negative Mutation Self-Tests: PASS"

echo ""
echo "[3/3] Auditing Build 3: Independent Agent Zero-Shot Build (377 pp.)"
python3 "skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py" \
  --kb "corpora/independent-agent-377pp/data/sheaf_kb.json" \
  --html "studios/independent-agent-zero-shot/index.html" \
  --query-script "corpora/independent-agent-377pp/query_sheaf.py" \
  --out "audits/independent_agent_r3_moe_audit.json"
python3 "skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py" \
  --kb "corpora/independent-agent-377pp/data/sheaf_kb.json" --selftest >/dev/null
echo "  ✓ Independent Agent 4/4 Negative Mutation Self-Tests: PASS"

echo ""
echo "================================================================================"
echo "  ALL 3 BUILDS VERIFIED: 27/27 BINARY GATES (GO) + 12/12 NEGATIVE SELFTESTS PASS"
echo "================================================================================"
