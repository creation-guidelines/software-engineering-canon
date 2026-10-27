<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Practices

Habits and tooling that make the principles and architectures stick.

<a id="enforce-boundaries"></a>
### Enforce boundaries with tooling

Use crate or project references, dependency-rule linters and architecture tests; documentation alone is not enough.

Serves
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

Pairs with
: [Prose may name, only code may claim](principles.md#prose-names-code-claims) (A boundary asserted in prose is a wish. Assert it in a test.)

<a id="adr"></a>
### Architecture decision records

Record each significant decision together with its context.

Pairs with
: [The why needs a carrier that cannot drift](principles.md#the-why-needs-a-carrier-that-cannot-drift) (An ADR records a decision at a date and does not claim to describe the present. Claims about the present belong to tests.)

<a id="test-at-the-seams"></a>
### Test at the seams

Fast core tests with in-memory adapters, contract tests per port, and few end-to-end tests.

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (In-memory adapters make core tests fast.)

Served by
: [Facts about the foreign world as tests](practices.md#executable-facts) (The adapter's tests are the documentation of the foreign world.)

<a id="twelve-factor"></a>
### Twelve-factor discipline

Keep configuration, logging and process handling disciplined and environment-independent.

<a id="observability"></a>
### Observability as a port

Structured logs, traces and metrics are a first-class outbound port, not an afterthought.

<a id="ci-gatekeeper"></a>
### CI as the gatekeeper

Format, lint, type-check and test on every change.

Pairs with
: [Ratchets for debt you cannot pay yet](practices.md#ratchet)

<a id="ratchet"></a>
### Ratchets for debt you cannot pay yet

Write the existing violations of a rule down with their size. Fail if any grows or a new one appears, and also fail when one shrinks until its entry is lowered or removed, so that progress is locked in and the list can only get shorter. The same helper serves every rule: file length (a smell that two levels share a file), printing outside the presenter, tool words in names.

Serves
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture) (A fitness function you can adopt over code that already breaks it.)

Pairs with
: [CI as the gatekeeper](practices.md#ci-gatekeeper)

Sources
: [Ratchets in software development](https://qntm.org/ratchet), [How we evolve code: Notion's ratcheting system using custom ESLint rules](https://www.notion.com/blog/how-we-evolved-our-code-notions-ratcheting-system-using-custom-eslint-rules), [ADR 20: Every module is a small language, and the outline is generated (measured baseline and ratchets)](https://github.com/grenudi/snapall/blob/main/docs/adr/0020-every-module-is-a-small-language.md)

<a id="generated-outline"></a>
### Generate the outline from the code

Produce the table of contents of the program (each module and the sentence it gives for what it is for) from the modules themselves, and fail the build if the committed copy differs. Likewise generate the command list, the completions and the manual from the declared contract. Prose written by no one cannot drift.

Serves
: [Derive, don't verify](principles.md#derive-dont-verify) (The outline is computed, never written.)

Pairs with
: [Prose may name, only code may claim](principles.md#prose-names-code-claims) (The outline is only as true as the sentences it is built from, so they may only name.)

Sources
: [Living Documentation by design, with Domain-Driven Design](https://leanpub.com/livingdocumentation), [OUTLINE.md: the generated outline of a whole program, from what each module says it is for](https://github.com/grenudi/snapall/blob/main/OUTLINE.md)

<a id="story-grammar"></a>
### Write stories in a grammar

A function at a high layer reads as a sequence of verbs on nouns: ask, do, record, say. Hide lifetimes, format strings, Option and Result plumbing, bare booleans and None arguments behind verbs named for what they mean, and cap how often a story branches and how many closures it spells out. Whatever language-level syntax remains marks a concept the layer has not named yet (a Stop, an Approved, a Said): name it.

Serves
: [Stratified design: every layer a small language](architectures.md#stratified-design)

Pairs with
: [Typestate](principles.md#typestate) (The missing noun is often a type: an Approved that only the answer to a question can produce.)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="cold-read"></a>
### The cold read

Give someone, or an agent, only the generated outline and the front files, and ask what the program does and what happens on one important action. Where they cannot say, a name is missing. It is the test of whether the code teaches. It is a procedure today and not yet an automated test.

Enforces
: [Stratified design: every layer a small language](architectures.md#stratified-design) (Tests whether the layers actually teach.)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="executable-facts"></a>
### Facts about the foreign world as tests

Record what is known about tools, systems and libraries as tests named as sentences, such as removing_an_area_deletes_every_snapshot_and_leaves_its_files, that run against the real thing in CI. They document the boundary and cannot drift: if the tool changes, the build says so.

Serves
: [Test at the seams](practices.md#test-at-the-seams) (The adapter's tests are the documentation of the foreign world.)

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="every-layer-is-a-top"></a>
### Every layer is the top of the layers beneath it

The same shape repeats at every level. A module says what it is for and offers a vocabulary (nouns and verbs) to the layer above, and its body is written only in the vocabulary of the layers beneath it, each of which is in turn the top of its own. Reading one module alone tells you its purpose and its words, and going down is always optional. Top is relative: the command line and the window are the top of the whole program, and a small adapter is the top of the tool it wraps. Layers form a graph and not a tree, since a lower layer is used by many above it, and the only structural rule is that dependencies point downward. A module that needs two languages, which means two levels, is two modules, whatever its length. Length, such as a file past a screen, is only a smell that a level is hiding. It is never the rule.

Serves
: [Stratified design: every layer a small language](architectures.md#stratified-design)

Pairs with
: [Screaming architecture](architectures.md#screaming-architecture) (Module and directory names that read as the program's purposes.)

Sources
: [Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html), [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)
