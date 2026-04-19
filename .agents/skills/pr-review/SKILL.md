---
name: pr-review
description: Deterministic pull-request review behavior for this repository
---

# pr-review

## Purpose

Define a deterministic checklist for reviewing pull requests in this repository.

## Review checklist

Every PR MUST be evaluated against the following items:

1. [ ] **Lint passes**: `ruff check . --fix` and `ruff format .` produce zero errors.
2. [ ] **Tests pass**: `pytest` runs successfully with zero failures.
3. [ ] **Type checking passes**: `mypy sphinx_no_pragma.py` produces no errors.
4. [ ] **RST validation passes**: `doc8` reports no errors (if documentation files changed).
5. [ ] **No secrets leaked**: `detect-secrets` baseline is not violated.
6. [ ] **Single responsibility**: The PR addresses a single, well-defined change.
7. [ ] **No breaking changes**: The public API (`DEFAULT_IGNORE_COMMENTS_ENDINGS`, `NoPragmaLiteralInclude`, `setup()`) is not altered without explicit justification.
8. [ ] **Documentation updated**: README, docs, or both are updated to match code changes.
9. [ ] **No unintended file changes**: No generated files (`.venv/`, `build/`, `dist/`, `htmlcov/`, etc.) are committed.
10. [ ] **Commit messages are descriptive**: Messages explain the "why", not just the "what".

## Must-check items

The reviewer **must** specifically check:

- Whether pragma stripping behavior is preserved or extended correctly.
- Whether `DEFAULT_IGNORE_COMMENTS_ENDINGS` changes are intentional and documented.
- Whether any new pragma markers added to the strip list are justified.
- Whether the `setup()` function's return dict (`version`, `parallel_read_safe`, `parallel_write_safe`) is unchanged.
- Whether example code in `examples/` and documentation still works.

## Reporting expectations

When reviewing a PR, the agent must:

- Report each checklist item as pass or fail.
- List specific failures with file paths, line numbers, and error messages.
- Suggest concrete fixes for each failure.
- State clearly whether the PR meets the Definition of Done.

## Exclusions

- Implementation guidance is the PR author's responsibility.
- Development workflow details (lint → fix → test loops) are handled by `dev-workflow/SKILL.md`.
