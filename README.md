# DevLens

[![CI](https://github.com/JoaoAlves20/DevLens/actions/workflows/ci.yml/badge.svg)](https://github.com/JoaoAlves20/DevLens/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**English** · [Português](README.pt-BR.md)

> Static engineering analysis for code repositories.

DevLens takes a Git repository (a public URL or a local path) and produces a technical
report about it: how it is structured, what it is built with, where its architecture
is fragile, what code is duplicated, which dependencies are vulnerable, and what to
improve first.

**It is not a chatbot that reads code.** Every finding comes from deterministic
analysis (parsing, dependency graphs, hashing and metrics), always points to the
exact file and line, and the same input always yields the same report.

> **Status:** early development (v0.0.1). See the [roadmap](#roadmap).

## Planned features

| Area | What DevLens reports |
|---|---|
| **Structure** | Directory tree, lines of code per language, largest files, project hygiene (tests, CI, docs) |
| **Technologies** | Languages, frameworks, build tools, CI and containers detected from manifests |
| **Architecture** | Dependency graph, circular dependencies, god modules, instability, complexity, layer-rule violations |
| **Rails** | Dependency graph inferred from Zeitwerk conventions, fat controllers / models, end-of-life Rails versions |
| **Duplication** | Copy-pasted code, including clones with renamed identifiers |
| **Diagrams** | Mermaid / Graphviz architecture diagrams and an interactive graph |
| **Dependencies** | Known vulnerabilities (OSV.dev), outdated packages, licenses |
| **Report** | Health score, prioritized findings with evidence, JSON / Markdown / HTML / SARIF |

Supported languages in v1: **Python**, **JavaScript / TypeScript** and **Ruby on Rails**.
More languages can be added as plugins.

## Ways to use it

```bash
devlens analyze https://github.com/owner/repo   # CLI report (Day 2+)
devlens serve                                   # local web UI (Day 13+)
```

The GitHub Action will comment on pull requests with the change in health score.
Everything runs locally: there is no hosted service. A static demo with pre-generated
reports will be published on GitHub Pages.

## Development

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/JoaoAlves20/DevLens.git
cd DevLens
uv sync                       # create the virtualenv and install dependencies
uv run pre-commit install     # run lint and type checks before every commit

uv run devlens --version
uv run pytest                 # tests + coverage
uv run ruff check .           # lint
uv run mypy                   # strict type checking
```

## How this project is built

DevLens is built by **João Alves acting as owner and AI orchestrator**, with Claude as
the implementer. Every product and architecture decision is made by the owner and
recorded:

- [AI_WORKFLOW.md](AI_WORKFLOW.md): roles, rules and the session loop
- [DECISIONS.md](DECISIONS.md): log of every decision
- [docs/adr/](docs/adr/): architecture decision records

## Roadmap

| Phase | Milestone | Content |
|---|---|---|
| 1. Engine and CLI | v0.1.0 | Ingestion, structure and technology detection |
| | v0.2.0 | Import graphs (Python, JS/TS, Ruby/Zeitwerk), architecture metrics, layer rules, Mermaid diagrams |
| | v0.3.0 | Duplication, dependencies and vulnerabilities, health score, reports |
| 2. Local web UI | v0.4.0 | `devlens serve`, dashboard, findings explorer, interactive graph |
| 3. Launch | v1.0.0 | GitHub Action, hotspots, static demo, PyPI release |

## License

[MIT](LICENSE)
