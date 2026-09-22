<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Architectures

Two independent axes: the macro structure of the system (modules and their boundaries) and the micro structure inside a module. Comparing them as rivals is a category error.

<a id="hexagonal"></a>
### Hexagonal architecture (ports and adapters)

The application core talks to the outside world only through ports, which are purposeful conversations; adapters plug technologies into ports. The application can be driven equally by users, programs, tests or batch jobs, and developed and tested in isolation from databases and UIs. The hexagon is only a drawing convention: it leaves room to add as many ports and adapters as needed, where a layered drawing forces a one-dimensional picture.

**Best when:** The default choice for most projects: infrastructure-independent, swappable components, and in-memory adapters that make tests trivial.

*Origin: Alistair Cockburn, 2005*

**Served by:** [SOLID](principles.md#solid) (Dependency inversion is the mechanism.)

**Same family as:** [Clean and onion architecture](architectures.md#clean-onion)

**Pairs with:** [Functional core, imperative shell](architectures.md#functional-core-imperative-shell), [Modular monolith](architectures.md#modular-monolith) (Macro structure (modules) and micro structure (inside a module) are independent axes.), [Test at the seams](practices.md#test-at-the-seams) (In-memory adapters make core tests fast.)

**Supplied by:** [Domain-driven design](architectures.md#ddd) (The domain model lives inside the hexagon.)

**Enforced by:** [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

**Sources:** [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture), [Hexagonal architecture pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

<a id="clean-onion"></a>
### Clean and onion architecture

The same dependency rule as hexagonal, expressed as concentric layers that point inward.

**Best when:** The same family as hexagonal; pick the vocabulary your team already has.

*Origin: Robert C. Martin and Jeffrey Palermo*

**Same family as:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal)

**Served by:** [SOLID](principles.md#solid) (Dependency inversion is the mechanism.)

<a id="functional-core-imperative-shell"></a>
### Functional core, imperative shell

Pure decision logic in the core; I/O and effects in a thin shell.

**Best when:** Pairs naturally with hexagonal and with type-driven design.

**Pairs with:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal)

**Sources:** [Building modern architectures: Functional Core, Imperative Shell](https://medium.com/@allousas/building-modern-architectures-functional-core-imperative-shell-revamp-0bb5ae62b589)

<a id="ddd"></a>
### Domain-driven design

Model the business language: bounded contexts, aggregates, value objects and a ubiquitous language.

**Best when:** Complex domains; it supplies the inside of the hexagon.

*Origin: Eric Evans, 2003*

**Supplies:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (The domain model lives inside the hexagon.)

<a id="vertical-slice"></a>
### Vertical slices

Organise code by feature or use case rather than by technical layer.

**Best when:** Change locality; CRUD-heavy or API-driven applications.

**Pairs with:** [Modular monolith](architectures.md#modular-monolith) (Slices organise the inside of a module.)

**Sources:** [Modules vs vertical slices: macro vs micro architecture](https://appscale.blog/en/blog/modules-vs-vertical-slices-macro-vs-micro-architecture-modular-monolith-2026)

<a id="modular-monolith"></a>
### Modular monolith

Real modules with enforced boundaries, deployed as one unit.

**Best when:** Most teams: it avoids the operating cost of microservices and keeps the option to extract services later.

**Pairs with:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (Macro structure (modules) and micro structure (inside a module) are independent axes.), [Vertical slices](architectures.md#vertical-slice) (Slices organise the inside of a module.)

**Enforced by:** [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

**Sources:** [Modules vs vertical slices: macro vs micro architecture](https://appscale.blog/en/blog/modules-vs-vertical-slices-macro-vs-micro-architecture-modular-monolith-2026)

<a id="cqrs-event-sourcing"></a>
### CQRS and event sourcing

Separate read and write models; keep state as a log of events.

**Best when:** Only where audit, temporal or scale needs justify the cost.

<a id="evolutionary-architecture"></a>
### Evolutionary architecture with fitness functions

Automated checks, such as dependency-rule tests and complexity or coupling budgets, keep the architecture honest.

**Best when:** Always: boundaries without enforcement rot into a big ball of mud.

**Enforces:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal), [Modular monolith](architectures.md#modular-monolith)

**Served by:** [Enforce boundaries with tooling](practices.md#enforce-boundaries)
