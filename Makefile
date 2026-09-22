# Guard/canon/SQL come from .tad/ (shared engine, see .tad/README.md). render is local to this
# repo - see .tad/README.md for why.
SHELL := /bin/bash
DC = python3 .tad/tools/dc.py

.PHONY: setup check checks canon render sql test verify
setup:            ## install pinned DuckDB + Miller
	./.tad/bootstrap.sh
check:            ## key guard: unknown or vanished JSON keys
	$(DC) check
checks:           ## invariant queries in checks/*.sql
	$(DC) checks
canon:            ## import -> validate -> canonical export
	$(DC) canon
render:           ## data/ -> docs/*.md (this repo's own renderer, not .tad/'s generic one)
	python3 tools/render.py
sql:              ## make sql Q="UPDATE ...; SELECT ..."
	$(DC) sql "$(Q)"
test:             ## tests for .tad/ itself
	python3 .tad/tests/test_dc.py
verify: check checks   ## what CI runs: data is valid and canonical, docs are fresh (works on uncommitted changes too)
	@before="$$(find data docs -type f -print0 | sort -z | xargs -0 sha256sum)"; \
	$(DC) canon && python3 tools/render.py; \
	after="$$(find data docs -type f -print0 | sort -z | xargs -0 sha256sum)"; \
	if [ "$$before" != "$$after" ]; then \
	  echo "data/ or docs/ was not canonical/fresh and has been rewritten. Review and commit:"; \
	  diff <(echo "$$before") <(echo "$$after") || true; exit 1; \
	fi; echo "verify: data canonical, docs fresh"
