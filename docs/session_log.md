<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Session Log

One entry per significant decision: what was done, what was considered, what was rejected and why.

<a id="research-then-seed-canon"></a>
### Researched engineering principles and seeded the canon

Date
: 2026-09-21

Done
: Web-researched sourced principles (DRY, KISS, parse-dont-validate, hexagonal architecture, etc.) and committed the first 15 principles, 8 architectures and 6 practices as a private GitHub repo (grenudi/design-canon).

<a id="storage-format-spike"></a>
### Spiked DuckDB + JSONL as the storage format on real content

Date
: 2026-09-21

Done
: Tested the format against this repo's real data specifically (not a toy example): schema changes, ALTER TABLE limits, a real semicolon-in-SQL bug, BLOB corruption, and 300k-row determinism on a real multi-core CI runner.

Considered
: Doltgres, Dolt, gitsheets, GlueSQL.

Rejected
: See tad-engine's and text-as-data-template's own session logs for the full comparison - this repo was the proving ground.

<a id="extract-shared-engine"></a>
### Extracted the proven tooling into text-as-data-template, then adopted it back

Date
: 2026-09-21

Done
: Moved dc.py, render.py and the invariant checks into a new template repo once they had been battle-tested here, then adopted that template's engine back into this repo via .tad/, keeping this repo's own render.py local since its output (grouped principles, "Watch out:", "Also known as:") is genuinely specific to this content.

<a id="migrate-subtree-to-subrepo"></a>
### Migrated the vendored engine from git subtree to git subrepo

Date
: 2026-09-22

Done
: Followed the same migration as text-as-data-template once subrepo was tested and adopted there.

<a id="rebuild-from-template"></a>
### Rebuilt this repo from a fresh generation of text-as-data-template

Date
: 2026-09-22

Done
: Renamed the original repo to software-engineering-canon-legacy, generated a new software-engineering-canon from the template via GitHub's actual template-generation API (not simulated), bootstrapped .tad/ with bin/adopt-engine.sh, and carried the real content and this custom render.py across - a battle test of the whole template pipeline end to end, at the request of the person running this project.

Considered
: Keep using the original repo as-is.

Rejected
: The point was specifically to prove a fresh repo generated from the template works for real, not simulated - this repo became that test.

<a id="adopt-rfc-style"></a>
### Adopted the RFC-like minimal style, engine part pulled and local part hand-ported

Date
: 2026-09-22

Done
: git subrepo pull brought the generic engine's definition-list render.py update cleanly, but this repo keeps its own local tools/render.py (deliberately, for its richer presentation), so the pull alone did nothing here - the same bold-to-definition-list edit had to be hand-applied to all 8 spots in this repo's own renderer. Added the matching _config.yml, _layouts/default.html and assets/css/style.css by hand too, since those are not vendored.

Considered
: Assuming the engine pull would cover the whole change here, since it covered it cleanly elsewhere.

Rejected
: Checked rather than assumed: grepped for bold markers in this repo's render.py right after the pull and found 8 still there, confirming the two repos needed genuinely different amounts of work for the same visual change.
