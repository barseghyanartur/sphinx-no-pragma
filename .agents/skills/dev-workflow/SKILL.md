---
name: dev-workflow
description: Definition of Done and development workflow procedures
---

## Definition of Done

A task is complete when:
1. All tests pass
2. All linting issues are resolved
3. Pre-commit hooks pass
4. Documentation is consistent with code changes

## Development Workflow

### Mandatory Sequence

1. **Lint** — Run linters and formatters first
2. **Fix** — Address all linting issues
3. **Test** — Run tests to verify the fix works
4. **Repeat** — Continue until both lint and tests pass

### Linting Commands (uv-based)

Run ruff:

```bash
make ruff
```

Or directly:

```bash
uv run ruff check . --fix
uv run ruff format .
```

Run mypy:

```bash
make mypy
```

Or directly:

```bash
uv run mypy sphinx_no_pragma.py
```

### Testing Commands

Run tests with pytest:

```bash
make quick-test
```

Or directly:

```bash
uv run pytest
```

### Pre-commit Commands

Run pre-commit hooks:

```bash
make pre-commit
```

Or directly:

```bash
pre-commit run --all-files
```

### Stop Conditions

Stop when:
- All tests pass
- No ruff errors or warnings remain
- Mypy reports no errors
- Pre-commit hooks pass on all files

### Forbidden Actions

- Never skip tests to complete a task
- Never commit with failing pre-commit hooks
- Never modify source code to bypass linting rules
