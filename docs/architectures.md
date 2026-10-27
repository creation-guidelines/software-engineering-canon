<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Architectures

Two independent axes: the macro structure of the system (modules and their boundaries) and the micro structure inside a module. Comparing them as rivals is a category error.

<a id="hexagonal"></a>
### Hexagonal architecture (ports and adapters)

The application core talks to the outside world only through ports, which are purposeful conversations; adapters plug technologies into ports. The application can be driven equally by users, programs, tests or batch jobs, and developed and tested in isolation from databases and UIs. The hexagon is only a drawing convention: it leaves room to add as many ports and adapters as needed, where a layered drawing forces a one-dimensional picture.

Best when
: The default choice for most projects: infrastructure-independent, swappable components, and in-memory adapters that make tests trivial.

Origin
: Alistair Cockburn, 2005

Served by
: [SOLID](principles.md#solid) (Dependency inversion is the mechanism.)

Same family as
: [Clean and onion architecture](architectures.md#clean-onion)

Pairs with
: [Functional core, imperative shell](architectures.md#functional-core-imperative-shell), [Modular monolith](architectures.md#modular-monolith) (Macro structure (modules) and micro structure (inside a module) are independent axes.), [Test at the seams](practices.md#test-at-the-seams) (In-memory adapters make core tests fast.), [Facts about the foreign world as tests](practices.md#executable-facts), [Stratified design: every layer a small language](architectures.md#stratified-design) (Hexagonal says where the boundary is. Stratified design says how every layer above it is written.)

Supplied by
: [Domain-driven design](architectures.md#ddd) (The domain model lives inside the hexagon.)

Enforced by
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

Sources
: [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture), [Hexagonal architecture pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

<a id="clean-onion"></a>
### Clean and onion architecture

The same dependency rule as hexagonal, expressed as concentric layers that point inward.

Best when
: The same family as hexagonal; pick the vocabulary your team already has.

Origin
: Robert C. Martin and Jeffrey Palermo

Same family as
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal)

Served by
: [SOLID](principles.md#solid) (Dependency inversion is the mechanism.)

<a id="functional-core-imperative-shell"></a>
### Functional core, imperative shell

Pure decision logic in the core; I/O and effects in a thin shell.

Best when
: Pairs naturally with hexagonal and with type-driven design.

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal)

Sources
: [Building modern architectures: Functional Core, Imperative Shell](https://medium.com/@allousas/building-modern-architectures-functional-core-imperative-shell-revamp-0bb5ae62b589)

<a id="ddd"></a>
### Domain-driven design

Model the business language: bounded contexts, aggregates, value objects and a ubiquitous language.

Best when
: Complex domains; it supplies the inside of the hexagon.

Origin
: Eric Evans, 2003

Supplies
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (The domain model lives inside the hexagon.)

Served by
: [Names are the person's words](principles.md#names-are-the-persons-words) (The ubiquitous language, applied to every name in the code.)

<a id="vertical-slice"></a>
### Vertical slices

Organise code by feature or use case rather than by technical layer.

Best when
: Change locality; CRUD-heavy or API-driven applications.

Pairs with
: [Modular monolith](architectures.md#modular-monolith) (Slices organise the inside of a module.)

Same family as
: [Screaming architecture](architectures.md#screaming-architecture) (Both organise by purpose rather than by technical layer.)

Sources
: [Modules vs vertical slices: macro vs micro architecture](https://appscale.blog/en/blog/modules-vs-vertical-slices-macro-vs-micro-architecture-modular-monolith-2026)

<a id="modular-monolith"></a>
### Modular monolith

Real modules with enforced boundaries, deployed as one unit.

Best when
: Most teams: it avoids the operating cost of microservices and keeps the option to extract services later.

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (Macro structure (modules) and micro structure (inside a module) are independent axes.), [Vertical slices](architectures.md#vertical-slice) (Slices organise the inside of a module.)

Enforced by
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

Sources
: [Modules vs vertical slices: macro vs micro architecture](https://appscale.blog/en/blog/modules-vs-vertical-slices-macro-vs-micro-architecture-modular-monolith-2026)

<a id="cqrs-event-sourcing"></a>
### CQRS and event sourcing

Separate read and write models; keep state as a log of events.

Best when
: Only where audit, temporal or scale needs justify the cost.

<a id="evolutionary-architecture"></a>
### Evolutionary architecture with fitness functions

Automated checks, such as dependency-rule tests and complexity or coupling budgets, keep the architecture honest.

Best when
: Always: boundaries without enforcement rot into a big ball of mud.

Enforces
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal), [Modular monolith](architectures.md#modular-monolith), [Stratified design: every layer a small language](architectures.md#stratified-design)

Served by
: [Enforce boundaries with tooling](practices.md#enforce-boundaries), [Ratchets for debt you cannot pay yet](practices.md#ratchet) (A fitness function you can adopt over code that already breaks it.)

<a id="stratified-design"></a>
### Stratified design: every layer a small language

Structure the system as levels, each described in its own language, with primitives, means of combination and means of abstraction fit for that level and built from the level below. A layer has nouns (the states it can be in, as types), verbs (the actions it offers) and a story that composes the verbs of the layer below, so its body names nothing two layers down. The stack ends where the language is not ours (compiler, libraries, operating system, tools) and each foreign thing is wrapped once, in our words, so that nothing above names it. Each level gives a different vocabulary for describing the system and a different kind of ability to change it. The shape is the same at every level: a layer is a part of the one above it and the top of those beneath it, so reading any single module tells you what it is for and what it offers.

Best when
: Programs meant to be learned by reading, and programs with several surfaces (command line, window, tests) over one core: the top layers read as the specification because they are the running code. It costs a layer of names, so remove any layer that only renames the one below.

Origin
: Harold Abelson and Gerald Jay Sussman

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (Hexagonal says where the boundary is. Stratified design says how every layer above it is written.)

Served by
: [Top layers decide which, when and where, never how](principles.md#top-layers-decide-which-not-how), [Write stories in a grammar](practices.md#story-grammar), [Every layer is the top of the layers beneath it](practices.md#every-layer-is-a-top)

Enforced by
: [The cold read](practices.md#cold-read) (Tests whether the layers actually teach.), [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

Sources
: [Structure and Interpretation of Computer Programs, 2.2.4 Example: A Picture Language (levels of language for robust design)](https://sicp.sourceacademy.org/chapters/2.2.4.html), [Every module is a small language (the rule, its procedure and its worked example)](https://github.com/grenudi/snapall/blob/main/docs/canon/small-languages.md)

<a id="screaming-architecture"></a>
### Screaming architecture

The structure of the code announces what the system is for, not what framework it runs on: a reader of the folder and module names should learn the use cases and still not know how the system is delivered. Delivery mechanisms, frameworks and databases are details kept at arm's length.

Best when
: Always, as the naming discipline of every layer above the adapters. It is the cheapest check of a stratified design: read the top-level names aloud.

Origin
: Robert C. Martin, 2011

Same family as
: [Vertical slices](architectures.md#vertical-slice) (Both organise by purpose rather than by technical layer.)

Pairs with
: [Every layer is the top of the layers beneath it](practices.md#every-layer-is-a-top) (Module and directory names that read as the program's purposes.)

Sources
: [Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html)
