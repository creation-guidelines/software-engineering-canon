<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->

# Practices

Habits and tooling that make the principles and architectures stick.

<a id="enforce-boundaries"></a>
### Enforce boundaries with tooling

Use crate or project references, dependency-rule linters and architecture tests; documentation alone is not enough.

Serves
: [Evolutionary architecture with fitness functions](architectures.md#evolutionary-architecture)

Served by
: [Test the guard](practices.md#test-the-guard) (A boundary check that has never failed has not been shown to enforce anything.)

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

Pairs with
: [Verify the published artifact](practices.md#verify-published-artifact) (CI proves what was built; this proves what was published.)

Served by
: [Test the documentation](practices.md#tested-documentation) (The gate covers documentation as well as code.)

<a id="reproducible-builds"></a>
### Reproducible builds

Pin the toolchain, remove build paths and timestamps from the output, and rebuild each release on another machine: a build that any party can repeat bit for bit is a build anyone can verify.

Serves
: [Verify the published artifact](practices.md#verify-published-artifact) (Reproducibility is what lets anyone rebuild a release and compare it with what was published.)

Sources
: [Definitions](https://reproducible-builds.org/docs/definition/)

<a id="verify-published-artifact"></a>
### Verify the published artifact

After a release, download what was actually published and check its checksums, its signed provenance and a fresh install, instead of trusting that the pipeline shipped what it tested.

Pairs with
: [CI as the gatekeeper](practices.md#ci-gatekeeper) (CI proves what was built; this proves what was published.)

Served by
: [Reproducible builds](practices.md#reproducible-builds) (Reproducibility is what lets anyone rebuild a release and compare it with what was published.)

Sources
: [SLSA: Provenance](https://slsa.dev/spec/v1.0/provenance)

<a id="tested-documentation"></a>
### Test the documentation

Treat documentation like code: one source for each fact, relative links checked in CI, examples compiled or run, and a test behind every claim a README or release note makes.

Serves
: [CI as the gatekeeper](practices.md#ci-gatekeeper) (The gate covers documentation as well as code.)

Sources
: [Docs as code](https://www.writethedocs.org/guide/docs-as-code/)

<a id="untrusted-generator-input"></a>
### Generators treat their input as untrusted

A generator that emits code (shell completions, SQL, configuration) validates names, quotes free text for the target language, and tests the output in the real interpreter, because its input is data someone else wrote.

Serves
: [Parse, don't validate](principles.md#parse-dont-validate) (A generator parses its input into trusted values before it writes any code.)

Sources
: [Injection Prevention - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)

<a id="test-the-guard"></a>
### Test the guard

A check that has never failed proves nothing: break what it guards on purpose and watch the check fail before relying on it.

Serves
: [Enforce boundaries with tooling](practices.md#enforce-boundaries) (A boundary check that has never failed has not been shown to enforce anything.)

Sources
: [Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)
