# 0002. Technology stack and repository layout

- **Status:** Accepted
- **Date:** 2026-11-22
- **Decided by:** João Alves

## Context

DevLens parses source code in several languages, builds dependency graphs, detects
duplicated code, queries vulnerability databases and renders reports, a web UI and
a GitHub Action. We need an ecosystem with strong static-analysis libraries, fast
iteration, and a credible modern front-end.

## Decision

| Concern | Choice | Why |
|---|---|---|
| Analysis engine | **Python ≥ 3.11** | Best static-analysis ecosystem: `tree-sitter` (one parser API for 40+ languages), `networkx` (graph algorithms), mature tooling |
| Parsing | **tree-sitter** | Uniform concrete syntax trees for Python, JS/TS and Ruby without writing parsers |
| CLI | **Typer + Rich** | Typed commands, good UX, trivial to test |
| API | **FastAPI + Pydantic** | Typed models shared with the engine, automatic OpenAPI |
| Web UI | **Next.js + TypeScript** (static export) | Modern front-end; exported to static files so it can be bundled into the Python package (see [0003](0003-local-first.md)) |
| Vulnerabilities | **OSV.dev API** | Free, no key, covers PyPI, npm and RubyGems |
| Tooling | **uv, ruff, mypy (strict), pytest + coverage, pre-commit, GitHub Actions** | Fast, reproducible, enforced locally and in CI |

Minimum Python is **3.11**; CI tests 3.11, 3.12, 3.13 and 3.14.

### Repository layout

```
src/devlens/      single installable Python package (engine, analyzers, CLI, API)
tests/            pytest suite
web/              Next.js front-end, exported and bundled into the package
action/           GitHub Action wrapping the CLI
docs/adr/         architecture decision records
```

The engine is a plain library with no dependency on the CLI, the API or the web UI.
Those are *adapters* that call into it (ports-and-adapters / hexagonal style), so the
same analysis runs identically from the terminal, the browser and a CI pipeline.

## Consequences

- One `pip install devlens` delivers everything a user needs.
- Python is slower than Go/Rust for very large repositories; if profiling shows a
  bottleneck, the hot path can be optimized or moved to a native extension later.
- Two languages in the repository (Python + TypeScript) means two toolchains in CI.
