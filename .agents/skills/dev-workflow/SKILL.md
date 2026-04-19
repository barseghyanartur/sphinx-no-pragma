---
name: dev-workflow
description: Definition of Done — lint, fix, test sequence with retry logic and stop conditions
---

# dev-workflow

## Purpose

Define the **Definition of Done** for any code change in this repository. This skill enforces the mandatory quality gate before any task is considered complete.

## Definition of Done

A change is **not done** until all of the following are satisfied:

1. Code changes are complete and self-consistent.
2. Linting passes with zero errors.
3. Tests pass with zero failures.
4. No regressions introduced.

## Mandatory sequence

Every code change MUST follow this exact sequence:

### Step 1 — Lint

```bash
ruff check . --fix
ruff format .
```

If `ruff check` reports remaining issues after `--fix`, fix them manually and re-run.

### Step 2 — Fix

Address any remaining lint issues that `--fix` could not auto-resolve. This includes:

- Style violations (`E`, `F` codes from pycodestyle/Pyflakes)
- Bugbear patterns (`B` codes)
- McCabe complexity issues (`C4`)
- Logging format errors (`G` codes)
- Import sorting issues (`I` codes)
- Naming convention violations (`ISC`, `N` codes)
- Performance issues (`PERF` codes)
- Simplify suggestions (`SIM` codes)
- TO-DO comment formatting (`TD` codes)

### Step 3 — Test

```bash
pytest
```

Or alternatively:

```bash
python -m unittest sphinx_no_pragma.py
```

### Step 4 — Re-lint

After fixing test failures, re-run lint to confirm clean state:

```bash
ruff check . --fix
ruff format .
```

## Retry logic

- If lint or tests fail, retry the fix cycle up to **3 times**.
- After 3 failed retry attempts, **stop** and report the blocker to the user.
- Do **not** skip tests or lint under any circumstances.

## Stop conditions

Stop and report to the user when:

- All lint passes and all tests pass (Definition of Done met).
- 3 retry attempts exhausted without resolving lint or test failures.
- A change cannot be completed without architectural decisions beyond the agent's scope.

## Forbidden actions

- **Never skip tests** to "save time."
- **Never disable lint rules** in `pyproject.toml` without explicit user approval.
- **Never commit code** that fails lint or tests.
- **Never bypass pre-commit hooks**.

## Project-specific notes

- The project also uses `mypy` for type checking. Run `mypy sphinx_no_pragma.py` when type-sensitive changes are made.
- RST documentation changes should be validated with `doc8`.
- Pre-commit hooks include: doc8, detect-secrets, pre-commit-hooks (trailing-whitespace, end-of-file-fixer, check-yaml, check-toml, check-added-large-files, debug-statements, check-merge-conflict), ruff-check, ruff-format.
