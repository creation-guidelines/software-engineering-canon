# software-engineering-canon

A curated canon of battle-tested software design principles, type-driven techniques and architectures, kept as an open, versioned, SQL-queryable dataset.

- **Read it:** https://creation-guidelines.github.io/software-engineering-canon/
- **Data:** [`data/`](data/) - one JSON-lines file per table, declared in [`tables.toml`](tables.toml).
- **Working on it (humans or agents):** read [`AGENTS.md`](AGENTS.md), run `make setup`, then `make verify`.

## How it works
`data/` is the source of truth. tad (a released Rust tool) checks it against `tables.toml`, edits it one checked row at a time, and writes it back in a canonical form so a one-row change is a one-line diff. CI checks that the data is valid and canonical, that every rule in [`tables.toml`](tables.toml) holds, and that the rendered [`docs/`](docs/) are up to date.

The reusable machinery (checking, canonical form, checked edits, rendering) is [tad](https://github.com/creation-guidelines/tad-engine), a released Rust tool. It began as this repository's own tooling, was extracted into a shared engine, and was rewritten in Rust in 2026.

## Releases
Commits follow [Conventional Commits](https://www.conventionalcommits.org/) and are linted on every PR; [release-please](https://github.com/googleapis/release-please) turns them into a changelog and tagged releases on `main`.

## Status
This repo was the design spike for [text-as-data-template](https://github.com/creation-guidelines/text-as-data-template). No license has been chosen yet.
