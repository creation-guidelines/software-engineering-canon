<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Practices

Habits and tooling that make the principles and architectures stick.

<a id="enforce-boundaries"></a>
### Enforce boundaries with tooling

Use crate or project references, dependency-rule linters and architecture tests; documentation alone is not enough.

Serves
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

<a id="adr"></a>
### Architecture decision records

Record each significant decision together with its context.

<a id="test-at-the-seams"></a>
### Test at the seams

Fast core tests with in-memory adapters, contract tests per port, and few end-to-end tests.

Pairs with
: [Hexagonal architecture (ports and adapters)](architectures.md#hexagonal) (In-memory adapters make core tests fast.)

<a id="twelve-factor"></a>
### Twelve-factor discipline

Keep configuration, logging and process handling disciplined and environment-independent.

<a id="observability"></a>
### Observability as a port

Structured logs, traces and metrics are a first-class outbound port, not an afterthought.

<a id="ci-gatekeeper"></a>
### CI as the gatekeeper

Format, lint, type-check and test on every change.
