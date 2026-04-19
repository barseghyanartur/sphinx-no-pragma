---
name: coding-standards
description: Style, typing, naming, logging, and error-handling rules for this repository
---

# coding-standards

## Purpose

Define the coding standards that govern this repository. These rules are non-negotiable and apply to all code contributions.

## Style rules

- **Black**: Line length of 80 characters. Target versions: py38 through py311. The file `docs/_static/example_1.py` is explicitly excluded.
- **Ruff**: Line length of 80 characters. autofix enabled (`fix = true`).
- **isort**: Black profile, combined imports, trailing commas, 80-char line length.

### Enforced ruff rule categories

The following categories are **selected** (enforced):

| Category | Meaning |
|---|---|
| `B` | Bugbear: common bugs and design issues |
| `C4` | McCabe complexity |
| `E` | pycodestyle style |
| `F` | Pyflakes: source errors |
| `G` | Logging format |
| `I` | Import sorting |
| `ISC` | String concatenation |
| `INP` | Implicit namespace packages |
| `N` | Naming conventions |
| `PERF` | Performance linting |
| `Q` | Quote handling |
| `SIM` | Code simplification |
| `TD` | TO-DO comments |

### Ignored ruff rules

| Rule | Reason |
|---|---|
| `G004` | Allow f-strings in logging statements |
| `ISC003` | Allow explicitly concatenated strings |
| `TD002` | TO-DO without author (optional) |
| `TD003` | TO-DO without URL (optional) |

## Typing rules

- **mypy** is configured with:
  - `check_untyped_defs = true` — all definitions must have types.
  - `warn_unused_ignores = true` — unused `# type: ignore` is an error.
  - `warn_redundant_casts = true` — unnecessary casts are flagged.
  - `warn_unused_configs = true` — unused mypy config sections are flagged.

## Naming conventions

- Python modules use `snake_case` (e.g., `sphinx_no_pragma.py`).
- Class names use `PascalCase` (e.g., `NoPragmaLiteralInclude`).
- Function and variable names use `snake_case`.
- Constants use `UPPER_SNAKE_CASE` (e.g., `DEFAULT_IGNORE_COMMENTS_ENDINGS`).

## Logging conventions

- Use Python's `logging` module.
- f-strings are allowed in logging statements (`G004` is ignored).
- Basic logging format errors (`G` codes) are selected but `G004` is excluded.

## Error-handling philosophy

- Use explicit error handling where appropriate.
- Do not suppress exceptions silently.
- `# type: ignore` and `# noqa` should be used sparingly and only when necessary — the purpose of this project is to reduce such pragmas in documentation.

## Enforcement

All rules are enforced automatically via:

- `ruff check . --fix` (lint)
- `ruff format .` (formatting)
- `mypy sphinx_no_pragma.py` (type checking)
- Pre-commit hooks (doc8, detect-secrets, pre-commit-hooks, ruff)

## Exclusions

- Procedural workflow (when to run these tools) is defined in `dev-workflow/SKILL.md`.
- Commands and tool invocation are defined in `dev-setup/SKILL.md`.
