<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Backlog

Known gaps in this canon, tracked the same way as its content.

## Open

<a id="choose-a-license"></a>
### Choose a license

No license chosen yet for this repo or the org overall.

<a id="source-remaining-concepts"></a>
### Source the remaining unsourced principles/architectures/practices

21 of 29 concepts have no entry in sources/concept_sources yet; see AGENTS.md for the backlog query.

<a id="grow-the-canon"></a>
### Grow the canon past its initial seed

20 principles, 10 architectures and 12 practices after the small-languages additions. Still a seed and not a comprehensive canon, which was the original goal.

<a id="small-languages-automate-cold-read"></a>
### Automate the cold read

The cold read is a procedure today: someone or an agent given only the generated outline and the entry points should be able to say what the program does and what happens on an important action. Open: run it in CI with fixed questions.

<a id="small-languages-bounds-are-smells"></a>
### Find out which size bounds really signal two languages in one module

The limits used in the source project (function 60, file 300, entry file 120, branching 4, closures 2) are alarms and were chosen to bite without blocking. Measure over more than one codebase which of them correlate with a module speaking two languages, and drop the ones that do not.

<a id="small-languages-foreign-layer"></a>
### Apply the discipline to the foreign layer

How the language, libraries and system calls are documented by the same discipline: executable facts per adapter, and how far generation can go without prose. Deferred by the author.

<a id="small-languages-doc-comments"></a>
### Decide whether doc comments beyond a one-line purpose can go

Whether the only prose in the code can be the one sentence per module that the outline is generated from, and what tooling then generates from names alone.

<a id="small-languages-second-language"></a>
### Test the rules in a second language

The rules were developed in one Rust codebase. Apply them to a project in another language to separate what is general from what is Rust.

<a id="small-languages-independent-evidence"></a>
### Find independent evidence for the project-specific rules

Prose may name and only code may claim, derive do not verify, story grammar and the cold read are supported by one project's experience and its own text. Look for independent sources or run a second experiment.
