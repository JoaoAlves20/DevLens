# 0001. Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-11-23
- **Decided by:** João Alves

## Context

DevLens is built by an AI implementer under the direction of a human owner (see
[AI_WORKFLOW.md](../../AI_WORKFLOW.md)). Because the owner does not write the code,
the *reasoning* behind each choice must be explicit, reviewable and durable. It is
also the main artifact the owner uses to explain the project.

## Decision

- Every decision goes into the one-line log in [DECISIONS.md](../../DECISIONS.md).
- Decisions with lasting architectural impact get an ADR in `docs/adr/`, numbered
  sequentially, using the format: Context → Decision → Consequences.
- ADRs are immutable once accepted. A change of mind is a new ADR that supersedes the
  old one (and the old one is marked `Superseded by NNNN`).

## Consequences

- Reviewers and interviewers can trace *why* the code looks the way it does.
- Small overhead per decision, kept low by the one-line log for minor choices.
