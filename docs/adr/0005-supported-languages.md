# 0005. Languages supported in v1

- **Status:** Accepted
- **Date:** 2026-11-22
- **Decided by:** João Alves

## Context

Supporting every language is an unbounded effort. We need a small set done well, and
an extension point for the rest.

## Decision

v1 supports **Python**, **JavaScript / TypeScript** and **Ruby (with Ruby on Rails)**.
Every language is implemented as a plugin behind a common interface, so new languages
can be added without touching the engine core.

### Ruby on Rails specifics

Rails code rarely uses explicit `require`: Zeitwerk autoloads constants by naming
convention (`Admin::UsersController` → `app/controllers/admin/users_controller.rb`).
A graph built only from `require` would be almost empty. DevLens therefore:

1. reads explicit `require` / `require_relative`;
2. **infers dependencies from constant references**, resolved to files using Zeitwerk
   naming conventions over the Rails autoload paths;
3. adds Rails-specific rules: oversized controllers and models, business logic in
   controllers, and Rails versions past end of life.

## Consequences

- Constant inference is heuristic: metaprogramming (`constantize`, `send`) cannot be
  resolved statically. Unresolved references are reported as such, never guessed.
- One extra implementation session is reserved for Ruby/Zeitwerk in the roadmap.
