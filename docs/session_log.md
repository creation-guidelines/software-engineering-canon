<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Session Log

One entry per significant decision: what was done, what was considered, what was rejected and why.

<a id="research-then-seed-canon"></a>
### Researched engineering principles and seeded the canon

*2026-09-21*

**Done:** Web-researched sourced principles (DRY, KISS, parse-dont-validate, hexagonal architecture, etc.) and committed the first 15 principles, 8 architectures and 6 practices as a private GitHub repo (grenudi/design-canon).

<a id="storage-format-spike"></a>
### Spiked DuckDB + JSONL as the storage format on real content

*2026-09-21*

**Done:** Tested the format against this repo's real data specifically (not a toy example): schema changes, ALTER TABLE limits, a real semicolon-in-SQL bug, BLOB corruption, and 300k-row determinism on a real multi-core CI runner.

**Considered:** Doltgres, Dolt, gitsheets, GlueSQL.

**Rejected:** See tad-engine's and text-as-data-template's own session logs for the full comparison - this repo was the proving ground.

<a id="extract-shared-engine"></a>
### Extracted the proven tooling into text-as-data-template, then adopted it back

*2026-09-21*

**Done:** Moved dc.py, render.py and the invariant checks into a new template repo once they had been battle-tested here, then adopted that template's engine back into this repo via .tad/, keeping this repo's own render.py local since its output (grouped principles, "Watch out:", "Also known as:") is genuinely specific to this content.

<a id="migrate-subtree-to-subrepo"></a>
### Migrated the vendored engine from git subtree to git subrepo

*2026-09-22*

**Done:** Followed the same migration as text-as-data-template once subrepo was tested and adopted there.

<a id="rebuild-from-template"></a>
### Rebuilt this repo from a fresh generation of text-as-data-template

*2026-09-22*

**Done:** Renamed the original repo to software-engineering-canon-legacy, generated a new software-engineering-canon from the template via GitHub's actual template-generation API (not simulated), bootstrapped .tad/ with bin/adopt-engine.sh, and carried the real content and this custom render.py across - a battle test of the whole template pipeline end to end, at the request of the person running this project.

**Considered:** Keep using the original repo as-is.

**Rejected:** The point was specifically to prove a fresh repo generated from the template works for real, not simulated - this repo became that test.
