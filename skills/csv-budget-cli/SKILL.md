---
name: csv-budget-cli
description: Use for this repository's CSV-based Python CLI budget app. Applies when editing code, tests, or project workflow for the budgetApp repo; enforces TDD, type hints, function length limits, cyclomatic complexity limits, and QA review with the qa_engineer subagent before commits.
---

# CSV Budget CLI

Use this skill when working in the `budgetApp` repository.

## Core workflow
- Read the existing code and tests before changing behavior.
- Write tests first, then implement the smallest change that makes them pass.
- Keep functions typed, short, and easy to review.
- Check complexity as you go; refactor before the code gets hard to reason about.
- Before committing, run a QA pass with the `qa_engineer` subagent.

## Rules to enforce
- Use type hints for every function and public method.
- Keep each function under 50 lines.
- Keep cyclomatic complexity at 10 or below.
- Prefer simple data structures and small helper functions.

## Validation
- Run `pytest` for behavior checks.
- Run `radon cc` for complexity review.
- If the change touches CSV parsing or transaction calculations, add focused tests for edge cases.

## Commit discipline
- Treat each finished feature as a commit boundary.
- Do not skip QA review before commit.
