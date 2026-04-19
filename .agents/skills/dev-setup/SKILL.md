---
name: dev-setup
description: Environment setup, dependency installation, and recovery steps for common environment failures
---

# dev-setup

## Purpose

Guide agents through environment setup, dependency installation, and recovery for this project.

## Project-specific setup

This project uses `uv` as the package manager and a `.venv/` virtual environment.

### Installing dependencies

```bash
uv pip install -e '.[all]'
```

Or using the Makefile:

```bash
make install
```

### Syncing dependencies

```bash
uv pip sync docs/requirements.txt
```

### Compiling requirements

```bash
make compile-requirements
make compile-requirements-upgrade
```

## Recovery steps

### Stale or broken virtual environment

If the virtual environment is broken or dependencies fail to resolve:

1. Remove the existing `.venv/` directory.
2. Recreate it with `uv pip install -e '.[all]'`.

### Missing tool commands

If `ruff`, `mypy`, `doc8`, or other tool commands are not found:

1. Ensure the virtual environment is activated (`.venv/bin/activate`).
2. Reinstall with `uv pip install -e '.[all]'`.

### Pre-commit hook failures

If pre-commit hooks fail:

1. Run the failing hook manually to see detailed output (e.g., `ruff check . --fix`).
2. Fix reported issues.
3. Re-run `pre-commit run --all-files`.

## Exclusions

- Coding rules are defined in `coding-standards/SKILL.md`.
- Test execution and PR review logic are defined in `dev-workflow/SKILL.md` and `pr-review/SKILL.md`.
