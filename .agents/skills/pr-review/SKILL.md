---
name: pr-review
description: Pull request review checklist and procedures
---

## Pull Request Review Checklist

1. **Tests pass**
   - All pytest tests pass
   - No skipped or ignored tests

2. **Linting clean**
   - ruff reports no errors
   - ruff format produces no changes
   - mypy reports no errors

3. **Pre-commit hooks pass**
   - All pre-commit hooks pass on modified files

4. **Code quality**
   - Code follows established patterns in the codebase
   - Type hints are present and correct
   - No hardcoded secrets or credentials

5. **Documentation**
   - Changes are reflected in appropriate documentation
   - Examples work correctly

6. **Security**
   - No secrets are committed
   - No security baselines are modified without cause

## Reporting

Report findings as:
- Issues with specific line numbers
- Suggested fixes when clear
- Questions when unclear
