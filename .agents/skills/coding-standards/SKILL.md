---
name: coding-standards
description: Code style, typing, naming, and error handling conventions
---

## Code Style

- Follow PEP 8 with line length of 80 characters
- Use Black for formatting (configured in pyproject.toml)
- Use isort for import sorting

## Typing Rules

- Use type hints for all function signatures
- Enable mypy strict mode
- Do not use `# type: ignore` unless absolutely necessary

## Naming Conventions

- Use snake_case for variables and functions
- Use PascalCase for classes
- Use SCREAMING_SNAKE_CASE for constants

## Error Handling

- Raise specific exceptions with clear messages
- Do not silently catch exceptions
- Log errors appropriately

## Enforcement

Code is validated by:
- ruff (linting and formatting)
- mypy (type checking)
- black (formatting)
- pre-commit hooks (automatic checks)