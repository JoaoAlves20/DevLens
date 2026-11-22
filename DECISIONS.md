# Decision Log

Every product and architecture decision in DevLens is made by the project owner
(**João Alves**). The AI pair (Claude) presents the options, the trade-offs and a
recommendation; the owner decides. See [AI_WORKFLOW.md](AI_WORKFLOW.md).

Larger decisions get a full Architecture Decision Record in [`docs/adr/`](docs/adr/).

| ID | Date | Decision | Chosen | Alternatives considered | ADR |
|----|------|----------|--------|-------------------------|-----|
| D-001 | 2026-11-22 | Technology stack | Python engine + FastAPI API + Next.js web | All-TypeScript; other stacks | [0002](docs/adr/0002-technology-stack.md) |
| D-002 | 2026-11-22 | Languages analyzed in v1 | Python, JavaScript/TypeScript, Ruby on Rails (others later via plugins) | Python + JS/TS only | [0005](docs/adr/0005-supported-languages.md) |
| D-003 | 2026-11-22 | Depth of Rails support | Full: `require` + Zeitwerk constant inference + Rails-specific rules | Generic Ruby only | [0005](docs/adr/0005-supported-languages.md) |
| D-004 | 2026-11-22 | v1.0 deliverables | CLI + local web UI + GitHub Action | CLI only; CLI + web | [0002](docs/adr/0002-technology-stack.md) |
| D-005 | 2026-11-22 | AI/LLM in the report | **None for now**; may be revisited later | Optional LLM summary; mandatory LLM | [0004](docs/adr/0004-no-llm-in-v1.md) |
| D-006 | 2026-11-22 | Repository sources | Public repositories + local paths | Private repos via GitHub OAuth | [0003](docs/adr/0003-local-first.md) |
| D-007 | 2026-11-22 | Project language | Code in English, README bilingual (EN / PT-BR) | English only; Portuguese only | — |
| D-008 | 2026-11-22 | Hosting | Local only + static demo on GitHub Pages | Free-tier backend deploy; paid hosting | [0003](docs/adr/0003-local-first.md) |
| D-009 | 2026-11-22 | Local web runtime | `devlens serve`: SQLite + in-process background jobs + bundled front-end | Docker Compose with Postgres + Redis + worker | [0003](docs/adr/0003-local-first.md) |
| D-010 | 2026-11-22 | Git workflow | One branch + PR per feature | Direct commits to `main` | — |
| D-011 | 2026-11-22 | AI transparency | Public `AI_WORKFLOW.md` | Not disclosed | — |
| D-012 | 2026-11-22 | License | MIT | — | — |
| D-013 | 2026-11-23 | Package / command name | `devlens` (fallback `devlens-cli` on PyPI if taken, command stays `devlens`) | `devlens-cli`, `dlens` | — |
| D-014 | 2026-11-23 | Minimum Python version | 3.11+ (CI tests 3.11 – 3.14) | 3.12+, 3.13+ | [0002](docs/adr/0002-technology-stack.md) |
| D-015 | 2026-11-23 | Commit / branch convention | Conventional Commits; branches `feat/…`, `fix/…`, `docs/…` | Scoped conventional commits; free-form | — |
| D-016 | 2026-11-23 | Commit author identity | Configured per repository with the owner's chosen e-mail | Global config by the owner | — |
| D-017 | 2026-11-23 | Who pushes and opens PRs | The AI commits, pushes and opens PRs (via GitHub CLI) | Owner pushes and opens PRs | — |
| D-018 | 2026-11-23 | Merge policy | The AI merges **only after explicit owner approval** and green CI | Auto-merge on green CI; owner merges on GitHub | — |
| D-019 | 2026-11-23 | Repository layout | Single installable Python package (`src/devlens`) holding engine, CLI and API; `web/` and `action/` as adapters | Separate `engine/` and `api/` top-level packages | [0002](docs/adr/0002-technology-stack.md) |
