# AGENTS.md — sphinx-no-pragma

## Project overview

A Sphinx extension that strips pragma comments (type: ignore, noqa, pragma: no cover, etc.) from source code included in documentation via `.. literalinclude::` directives.

## Architecture invariants

- Single-module package: `sphinx_no_pragma.py`
- Sphinx directive override: `literalinclude` directive
- Configuration via Sphinx `conf.py`: `ignore_comments_endings` and `user_ignore_comments_endings`
- Python 3.10+ required

## Repository layout (authoritative)

```
.
├── sphinx_no_pragma.py    # Main extension module
├── tests.py               # Test suite (unittest/pytest)
├── examples/              # Example code files
├── docs/                  # Sphinx documentation source
├── Makefile               # Build and task automation
├── pyproject.toml         # Project configuration
└── .pre-commit-config.yaml
```

## Hard constraints

- Do not modify source code to match documentation
- Documentation must reflect actual API/CLI behavior
- Code blocks in RST files may be tested via pytest-codeblock
- Pre-commit hooks must pass before commit

## Known intentional behaviors — do not change

- Pragma markers stripped: `# type: ignore`, `# noqa`, `# pragma: no cover`, `# pragma: no branch`, `# fmt: off/on/skip`, `# yapf: disable/enable`, `# pylint: disable/enable`, `# flake8: noqa`, `# noinspection`, `# pragma: allowlist secret`, `# pragma: NOSONAR`
- Default behavior can be overridden via `ignore_comments_endings` in `conf.py`
- Additional markers can be appended via `user_ignore_comments_endings` in `conf.py`
- Version: 0.1.3

## Configuration authority

- `pyproject.toml` is authoritative for dependencies and tool configuration
- `Makefile` is authoritative for build commands
- `.pre-commit-config.yaml` is authoritative for pre-commit hooks

## Agent obligations

- Run tests (pytest) and ensure they pass
- Run linting (ruff, black, mypy) and fix all issues
- Run pre-commit hooks before considering work complete
- Preserve existing documentation tests (pytest-codeblock)
- Never commit secrets or modify `.secrets.baseline`
