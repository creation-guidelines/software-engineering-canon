<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Principles

Small, sharp rules that hold up across languages and eras, followed by the type-driven techniques that let the compiler enforce them.

## Core principles

<a id="separation-of-concerns"></a>
### Separation of concerns, high cohesion, low coupling

Things that change together live together; things that do not, do not know each other.

Watch out
: The root of most of the other principles in this canon.

Served by
: [Top layers decide which, when and where, never how](principles.md#top-layers-decide-which-not-how) (Which, when and where above. How below.)

<a id="solid"></a>
### SOLID

Five object-oriented design principles; the two with the widest reach are single responsibility (one reason to change per module) and dependency inversion (depend on abstractions you own).

Watch out
: Dependency inversion is the mechanism behind hexagonal and clean architecture.

Origin
: Robert C. Martin

Serves
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (Dependency inversion is the mechanism.), [Clean and onion architecture](architectures.md#clean-onion) (Dependency inversion is the mechanism.)

<a id="composition-over-inheritance"></a>
### Composition over inheritance

Assemble behaviour from parts instead of inheriting it.

<a id="fail-fast"></a>
### Fail fast

Reject bad input at the boundary, loudly.

<a id="least-astonishment"></a>
### Principle of least astonishment

Behaviour matches what the name promises.

<a id="dry"></a>
### DRY

Every piece of knowledge has one authoritative home.

Also known as
: Don't repeat yourself

Watch out
: It is about knowledge, not textual similarity. A wrong abstraction costs more than duplication, so wait for the rule of three.

Origin
: Andy Hunt and Dave Thomas, 1999

Served by
: [Derive, don't verify](principles.md#derive-dont-verify) (DRY gives knowledge one home. This says what to do when a second copy is needed: compute it.), [The why needs a carrier that cannot drift](principles.md#the-why-needs-a-carrier-that-cannot-drift) (A reason is knowledge too: give it a home that is checked or generated.)

<a id="kiss"></a>
### KISS

The simplest thing that satisfies the actual requirement.

Also known as
: Keep it simple, stupid

Watch out
: Simple is not the same as easy. Measure simplicity by the number of concepts a reader must hold.

<a id="yagni"></a>
### YAGNI

Do not build for speculative futures.

Also known as
: You aren't gonna need it

Watch out
: It does not forbid clean seams: a port is a cheap boundary, not speculation.

<a id="demeter"></a>
### Law of Demeter, tell don't ask

Talk to your neighbours, not to their internals.

Also known as
: Principle of least knowledge

Origin
: Ian Holland, 1987

Sources
: [Law of Demeter (General Formulation)](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/general-formulation.html)

<a id="names-are-the-persons-words"></a>
### Names are the person's words

Name nouns and verbs as the people who use the system say them (area, snapshot, restore point), never by a design pattern (Manager, Helper, Util) and never by a tool's vocabulary above the code that wraps the tool.

Also known as
: Ubiquitous language in code

Watch out
: Where a tool's word and the person's word differ, the difference is a translation owed at the boundary. If it leaks upward the language splits in two: in snapall the core still says config where people say protected area, and the debt is tracked by a ratchet. The ubiquitous language of domain-driven design is this discipline applied to the domain model.

Serves
: [Domain-driven design](architectures.md#ddd) (The ubiquitous language, applied to every name in the code.)

Sources
: [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html), [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="derive-dont-verify"></a>
### Derive, don't verify

Where a fact is needed in several places, declare it once and compute the rest. A test that compares two hand-written copies means a copy should be removed. Keep tests for what cannot be derived (two modules that may not depend on each other, say) and write them against the single declaration.

Watch out
: Derivation needs somewhere to derive from: a table, a macro, a type. If building it costs more than the drift it prevents, a test over two copies is the honest fallback. Say so, and keep it small.

Serves
: [DRY](principles.md#dry) (DRY gives knowledge one home. This says what to do when a second copy is needed: compute it.)

Served by
: [Generate the outline from the code](practices.md#generated-outline) (The outline is computed, never written.)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="prose-names-code-claims"></a>
### Prose may name, only code may claim

A module's description says what it is about, as a noun phrase. A guarantee (only, never, always) belongs in a test or a type, where it can fail. In prose it can be false while the build stays green.

Watch out
: Found in practice: a module described as the one place output leaves the program while seven others printed by themselves, which a ratchet exposed. The rule is about guarantees, not about all prose: descriptions of subject stay useful and cheap. The same drift was found a second time when the worked example in the source text went stale the moment a type was renamed. A test now requires the example to equal the source it shows, and fails when it does not.

Pairs with
: [Enforce boundaries with tooling](practices.md#enforce-boundaries) (A boundary asserted in prose is a wish. Assert it in a test.), [Generate the outline from the code](practices.md#generated-outline) (The outline is only as true as the sentences it is built from, so they may only name.)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md), [ADR 20: Every module is a small language, and the outline is generated (measured baseline and ratchets)](https://github.com/grenudi/snapall/blob/main/docs/adr/0020-every-module-is-a-small-language.md)

<a id="top-layers-decide-which-not-how"></a>
### Top layers decide which, when and where, never how

Higher layers keep only the logic of choosing between named outcomes, ordering steps, arranging what sits where and streaming inputs to results. Each piece of how lives in the lowest layer that can state it without knowing the layer above. A line at the top then reads as common sense and is also the running implementation.

Watch out
: This is not no logic at the top: the top does branch, in the smallest portions and in domain words. If a top-layer function needs a paragraph, or a closure to plumb an Option, a verb is missing in the layer below.

Serves
: [Separation of concerns, high cohesion, low coupling](principles.md#separation-of-concerns) (Which, when and where above. How below.), [Stratified design: every layer a small language](architectures.md#stratified-design)

Sources
: [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="the-why-needs-a-carrier-that-cannot-drift"></a>
### The why needs a carrier that cannot drift

Reasons, decisions and facts about the foreign world should live where they are checked or generated: in names and types (a Destroys weight is a reason), in tests named as sentences that run against the real thing, and in outlines generated from the code. A machine-readable annotation (TODO with an owner, a safety note, an attribute) is not a comment in this sense.

Watch out
: Contested. Ousterhout argues that it is not possible to describe in code everything people need to know to understand it, and that comments should record what is not obvious. Martin's Clean Code treats most comments as a failure to express the idea in code. This canon takes the stronger position as a discipline and not as a law: look for a name, a type or a named executable fact first, and write a comment only when none can carry the reason, then keep it beside what it explains. Revisit if the discipline costs more than the drift it prevents.

Serves
: [DRY](principles.md#dry) (A reason is knowledge too: give it a home that is checked or generated.)

Pairs with
: [Architecture decision records](practices.md#adr) (An ADR records a decision at a date and does not claim to describe the present. Claims about the present belong to tests.)

Sources
: [John Ousterhout on A Philosophy of Software Design (Software Engineering Radio episode 520, transcript excerpts)](https://nikit.tcl-lang.org/page/%7BJohn+Ousterhout+on+A+Philosophy+of+Software+Design%7D+%7BSoftware+Engineering+Radio%7D+%7Bepisode+520%7D+%7B2022+07+12%7D), [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

## Type-driven design

<a id="illegal-states-unrepresentable"></a>
### Make illegal states unrepresentable

Model the domain so that invalid combinations cannot be expressed. Prefer sum types over flag soup.

Watch out
: Not every constraint fits the type system; when one does not, fall back to a smart constructor.

Origin
: Yaron Minsky

Served by
: [Parse, don't validate](principles.md#parse-dont-validate) (The boundary-facing, dynamic side of the same idea.), [Newtypes and typed primitives](principles.md#newtypes), [Typestate](principles.md#typestate)

Sources
: [Make illegal states unrepresentable](https://deviq.com/principles/make-illegal-states-unrepresentable/)

<a id="parse-dont-validate"></a>
### Parse, don't validate

Turn untrusted input into a precise type once, at the boundary; downstream code never re-checks.

Watch out
: Validation throws away its proof; parsing keeps it in the type. Where the type system cannot express a constraint, use an abstract newtype with a smart constructor and use judgement.

Origin
: Alexis King, 2019

Serves
: [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable) (The boundary-facing, dynamic side of the same idea.)

Sources
: [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)

<a id="newtypes"></a>
### Newtypes and typed primitives

Use Email, UserId or Cents instead of raw string and int. Smart constructors are the only way in.

Watch out
: The cure for primitive obsession.

Serves
: [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable)

Sources
: [Make illegal states unrepresentable](https://deviq.com/principles/make-illegal-states-unrepresentable/)

<a id="typestate"></a>
### Typestate

Encode state machines in types: transitions are functions between distinct types, for example Draft to Submitted.

Serves
: [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable)

Pairs with
: [Write stories in a grammar](practices.md#story-grammar) (The missing noun is often a type: an Approved that only the answer to a question can produce.)

<a id="total-functions"></a>
### Total functions and explicit errors

Use Result and Option; keep hidden exceptions and nulls out of the domain.

<a id="immutability"></a>
### Immutability by default

Data is immutable unless there is a reason; invariants are encapsulated behind private constructors.
