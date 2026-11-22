# 0003. Local-first: no hosted backend

- **Status:** Accepted
- **Date:** 2026-11-22
- **Decided by:** João Alves

## Context

A hosted DevLens instance on a free tier would suffer from cold starts (30–60 s after
idling), ~512 MB of RAM (too little to clone and analyze medium repositories),
expiring free databases and exposure to abuse. A paid instance has a recurring cost
the project does not need.

## Decision

1. **DevLens runs on the user's machine.** Sources are public Git repositories (cloned
   locally) or local paths. Private repositories / OAuth are out of scope for v1.
2. **The web UI is served locally with `devlens serve`**:
   - SQLite for persistence;
   - background jobs executed in-process (no Redis, no separate worker);
   - the front-end is pre-built and shipped inside the Python package.
   No Docker is required.
3. **A static demo is published on GitHub Pages**: pre-generated reports of a few
   well-known open-source repositories, so anyone can see DevLens without installing it.

## Alternatives considered

- **Free-tier deploy** (Render / Fly.io + Vercel): rejected for the reasons above.
- **Docker Compose with Postgres + Redis + worker**: shows more infrastructure, but is
  over-engineered for a single-user local tool and forces users to install Docker.

## Consequences

- Installation is one command; nothing to operate or pay for.
- Analysis jobs share the server process, which is acceptable for one local user.
  The job runner sits behind an interface so a real queue could replace it later.
- The public demo cannot analyze arbitrary repositories on demand.
