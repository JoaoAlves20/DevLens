# 0004. No LLM inside DevLens (for now)

- **Status:** Accepted
- **Date:** 2026-11-22
- **Decided by:** João Alves

## Context

Many "code analysis" tools are chat interfaces over an LLM. Their findings are not
reproducible, can be hallucinated and cost money per run. DevLens aims to be an
engineering tool, not a chatbot.

## Decision

DevLens v1 contains **no LLM**. Every finding is produced by deterministic analysis
(parsing, graph algorithms, hashing, metrics, vulnerability databases), always comes
with concrete evidence (file and line), and the same input always yields the same
report.

This may be revisited after v1. Any future LLM feature will be a separate ADR.

## Consequences

- Reports are reproducible, auditable and free to generate.
- DevLens works fully offline (except for cloning and the vulnerability lookup).
- Suggestions in the report come from rule templates, so they are less "conversational".
