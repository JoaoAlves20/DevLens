# AI Workflow

DevLens is built with an explicit division of labour between a human and an AI:

| Role | Who | Responsibilities |
|------|-----|------------------|
| **Owner / orchestrator** | João Alves | Product vision, scope, every architecture and product decision, acceptance of each deliverable, approval of every merge |
| **Implementer** | Claude (Anthropic), via Claude Code | Writing all code, tests and documentation; presenting options and trade-offs; running the tooling; committing, pushing and opening PRs |

The goal of the project is twofold: to build a useful engineering tool, and to
demonstrate how a developer can **orchestrate an AI** to deliver a production-grade
project while keeping full ownership of the decisions.

## Rules of engagement

1. **The AI never decides silently.** Any choice that affects the product, the
   architecture or the public surface is presented as options + trade-offs +
   recommendation, and waits for the owner.
2. **Every decision is recorded** in [DECISIONS.md](DECISIONS.md); larger ones get an
   [ADR](docs/adr/).
3. **Nothing reaches `main` without approval.** Work happens on a feature branch, CI
   must be green, and the AI merges only after the owner explicitly approves.
4. **Quality gates are automated.** Ruff (lint + format), mypy (strict) and pytest with
   a coverage floor run locally (pre-commit) and in CI on every PR.
5. **The analysis engine is deterministic.** DevLens does not use an LLM to produce
   findings (see [ADR 0004](docs/adr/0004-no-llm-in-v1.md)); the AI is used to *build*
   the tool, not inside it.

## Session loop

Work is organized in numbered sessions ("Day 1", "Day 2", …) following the roadmap in
the README. Each session follows the same loop:

```
 owner opens "Day N"
        │
        ▼
 AI presents the decisions of the day (options · trade-offs · recommendation)
        │
        ▼
 owner decides  ──►  recorded in DECISIONS.md / ADR
        │
        ▼
 AI implements code + tests, runs lint / types / tests locally
        │
        ▼
 AI pushes a branch and opens a PR ──► CI
        │
        ▼
 owner reviews and says "approved"  ──►  AI merges
```

## What the owner reviews

- Does the behaviour match the decision that was made?
- Are the trade-offs still acceptable now that the code exists?
- Is anything in the PR outside the agreed scope?
- Does the demo (CLI output, report, UI) look right on a real repository?
