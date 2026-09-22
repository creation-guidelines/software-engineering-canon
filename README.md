# software-engineering-canon

A curated canon of battle-tested software design principles, type-driven techniques and architectures, kept as an open, versioned, SQL-queryable dataset.

- **Read it:** https://creation-guidelines.github.io/software-engineering-canon/
- **Data:** [`data/`](data/) - `schema.sql`, `load.sql` and one JSON-lines file per table (DuckDB `EXPORT DATABASE`).
- **Working on it (humans or agents):** read [`AGENTS.md`](AGENTS.md), run `make setup`, then `make verify`.

## How it works
`data/` is the source of truth. DuckDB loads it in memory, SQL edits it, and it is written back in a canonical form so a one-row change is a one-line diff. CI checks that the data is valid and canonical, that invariants in [`checks/`](checks/) hold, and that the rendered [`docs/`](docs/) are up to date.

The reusable safety machinery (the guard, canonicalizer and SQL runner) lives in [`.tad/`](.tad/README.md), extracted from this repo into [creation-guidelines/text-as-data-template](https://github.com/creation-guidelines/text-as-data-template). `tools/render.py` stays local to this repo rather than living in `.tad/`, because this content's presentation (grouping principles by category, "Watch out:", "Also known as:") is genuinely specific to it.

## Releases
Commits follow [Conventional Commits](https://www.conventionalcommits.org/) and are linted on every PR; [release-please](https://github.com/googleapis/release-please) turns them into a changelog and tagged releases on `main`.

## Status
This repo was the design spike for [text-as-data-template](https://github.com/creation-guidelines/text-as-data-template). No license has been chosen yet.
