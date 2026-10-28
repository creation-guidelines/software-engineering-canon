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

<a id="small-languages-added"></a>
### Added the every-module-is-a-small-language findings from snapall

Date
: 2026-10-27

Done
: Added stratified design and screaming architecture, five principles and six practices, with 10 sources that were opened and read, 21 relations and their citations. The findings come from building snapall (a Rust snapshot tool) to the rule that every layer is a small language and that the code, not prose, is the specification. During the work the author corrected the first wording: front file and file length were written as two rules with two bounds, when the principle is that every layer is the top of the layers beneath it, so one module speaks one language and length is only a smell. The entry was rewritten before it was committed.

Considered
: Adding all sixteen rules of the source text as separate concepts. Giving the numeric bounds the status of rules. Putting the comments position in as settled. Adding a new principles category, which the schema constraint would have needed a hand edit for.

Rejected
: Rules as a checklist: this canon holds concepts and the source text keeps the procedure. Fixed size limits as the definition of a good module: they are alarms and the source project keeps them as ratchets for that reason. The comments position as a law: Ousterhout disagrees in the transcript cited and both views are recorded in the caveat.

<a id="small-languages-as-an-idea"></a>
### Restated the small-languages findings as one idea and not a list of rules

Date
: 2026-10-27

Done
: The author preferred the principle to a numbered rule list. The source text in snapall was rewritten as prose around the two faces of a layer, and this canon now leads stratified design with them: each layer has an upward face (what it is for and the words it offers) and a downward face (a body in the words of the layers beneath), and a layer below is the top of those under it. The source project continued the refactor under it: a missing noun found by reading a story (Stopped), modules split by language (one per command, and a four-language adapter file into four), with its size checks relabelled as alarms.

Considered
: Keeping the sixteen rules as the shape of the canon text, as a checklist beside the concepts.

Rejected
: A rule list as the shape of the source text: the rules are consequences of one idea and its alarms, and a list invites meeting them without understanding. The numeric limits as definitions: they find candidates and a short file that mixes two levels is still wrong.

<a id="small-languages-evidence-from-a-wide-rename"></a>
### Recorded what a wide rename and the next noun taught

Date
: 2026-10-28

Done
: Added the practice of capturing a program's output before a behaviour-preserving change and comparing it after, with Fowler's definition of refactoring and an engineering account of characterization tests as sources, and the source project's pull request as the worked case: 81 names and about 2,000 occurrences renamed so that the core says area and location where it said config and subvolume, with 24 commands compared byte for byte. Recorded Approved as the noun found after Stopped, and a second case of prose drifting from code (the worked example in the source text, now tested to equal the source it shows).

Considered
: Recording the rename as a refactoring catalogue entry: it is a technique for proving that a change preserved behaviour, not a move in itself.

Rejected
: Trusting the compiler and the unit tests alone for a rename this wide: neither sees what a user or a script can observe, and a variable renamed into a scope that already has that name changes meaning without an error.
