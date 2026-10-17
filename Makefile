.PHONY: verify selftest build-studios synthesize-audio help

help:
	@echo "CETI Sheaf Knowledge Studio — Available Targets:"
	@echo "  make verify            Run 26-gate MOE audit + 4/4 negative selftests across all 3 builds"
	@echo "  make selftest          Run contract linter negative-mutation selftests on all 3 KBs"
	@echo "  make build-studios     Compile all 3 interactive Field-Manual HTML Studios"
	@echo "  make synthesize-audio  Synthesize Dual-Host Neural Podcast MP3s (Kore x Puck) across all 3 KBs"

verify:
	@bash ./verify_all.sh

selftest:
	python3 skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py --kb corpora/spivak-609pp/data/sheaf_kb.json --selftest
	python3 skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py --kb corpora/marinov-377pp/data/sheaf_kb.json --selftest
	python3 skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py --kb corpora/independent-agent-377pp/data/sheaf_kb.json --selftest

build-studios:
	python3 skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py \
		--kb corpora/spivak-609pp/data/sheaf_kb.json \
		--out studios/spivak-category-theory-for-the-sciences/index.html \
		--bundle studios/spivak-category-theory-for-the-sciences/data/sheaf_pages_bundle.js
	python3 corpora/marinov-377pp/build_illustrated_studio_html.py
	python3 skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py \
		--kb corpora/independent-agent-377pp/data/sheaf_kb.json \
		--out studios/independent-agent-zero-shot/index.html \
		--bundle studios/independent-agent-zero-shot/data/sheaf_pages_bundle.js

synthesize-audio:
	/Users/cairo/.local/bin/uv run --with edge-tts python3 skills/sheaf-field-manual-studio/scripts/synthesize_notebook_podcast.py --kb corpora/spivak-609pp/data/sheaf_kb.json
	/Users/cairo/.local/bin/uv run --with edge-tts python3 skills/sheaf-field-manual-studio/scripts/synthesize_notebook_podcast.py --kb corpora/marinov-377pp/data/sheaf_kb.json
	/Users/cairo/.local/bin/uv run --with edge-tts python3 skills/sheaf-field-manual-studio/scripts/synthesize_notebook_podcast.py --kb corpora/independent-agent-377pp/data/sheaf_kb.json
