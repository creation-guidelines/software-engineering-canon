<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Principles

Small, sharp rules that hold up across languages and eras, followed by the type-driven techniques that let the compiler enforce them.

## Core principles

<a id="separation-of-concerns"></a>
### Separation of concerns, high cohesion, low coupling

Things that change together live together; things that do not, do not know each other.

**Watch out:** The root of most of the other principles in this canon.

<a id="solid"></a>
### SOLID

Five object-oriented design principles; the two with the widest reach are single responsibility (one reason to change per module) and dependency inversion (depend on abstractions you own).

**Watch out:** Dependency inversion is the mechanism behind hexagonal and clean architecture.

*Origin: Robert C. Martin*

**Serves:** [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (Dependency inversion is the mechanism.), [Clean and onion architecture](architectures.md#clean-onion) (Dependency inversion is the mechanism.)

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

**Also known as:** Don't repeat yourself

**Watch out:** It is about knowledge, not textual similarity. A wrong abstraction costs more than duplication, so wait for the rule of three.

*Origin: Andy Hunt and Dave Thomas, 1999*

<a id="kiss"></a>
### KISS

The simplest thing that satisfies the actual requirement.

**Also known as:** Keep it simple, stupid

**Watch out:** Simple is not the same as easy. Measure simplicity by the number of concepts a reader must hold.

<a id="yagni"></a>
### YAGNI

Do not build for speculative futures.

**Also known as:** You aren't gonna need it

**Watch out:** It does not forbid clean seams: a port is a cheap boundary, not speculation.

<a id="demeter"></a>
### Law of Demeter, tell don't ask

Talk to your neighbours, not to their internals.

**Also known as:** Principle of least knowledge

*Origin: Ian Holland, 1987*

**Sources:** [Law of Demeter (General Formulation)](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/general-formulation.html)

## Type-driven design

<a id="illegal-states-unrepresentable"></a>
### Make illegal states unrepresentable

Model the domain so that invalid combinations cannot be expressed. Prefer sum types over flag soup.

**Watch out:** Not every constraint fits the type system; when one does not, fall back to a smart constructor.

*Origin: Yaron Minsky*

**Served by:** [Parse, don't validate](principles.md#parse-dont-validate) (The boundary-facing, dynamic side of the same idea.), [Newtypes and typed primitives](principles.md#newtypes), [Typestate](principles.md#typestate)

**Sources:** [Make illegal states unrepresentable](https://deviq.com/principles/make-illegal-states-unrepresentable/)

<a id="parse-dont-validate"></a>
### Parse, don't validate

Turn untrusted input into a precise type once, at the boundary; downstream code never re-checks.

**Watch out:** Validation throws away its proof; parsing keeps it in the type. Where the type system cannot express a constraint, use an abstract newtype with a smart constructor and use judgement.

*Origin: Alexis King, 2019*

**Serves:** [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable) (The boundary-facing, dynamic side of the same idea.)

**Sources:** [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)

<a id="newtypes"></a>
### Newtypes and typed primitives

Use Email, UserId or Cents instead of raw string and int. Smart constructors are the only way in.

**Watch out:** The cure for primitive obsession.

**Serves:** [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable)

**Sources:** [Make illegal states unrepresentable](https://deviq.com/principles/make-illegal-states-unrepresentable/)

<a id="typestate"></a>
### Typestate

Encode state machines in types: transitions are functions between distinct types, for example Draft to Submitted.

**Serves:** [Make illegal states unrepresentable](principles.md#illegal-states-unrepresentable)

<a id="total-functions"></a>
### Total functions and explicit errors

Use Result and Option; keep hidden exceptions and nulls out of the domain.

<a id="immutability"></a>
### Immutability by default

Data is immutable unless there is a reason; invariants are encapsulated behind private constructors.
