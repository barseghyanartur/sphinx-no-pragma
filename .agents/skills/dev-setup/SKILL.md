---
name: dev-setup
description: Environment setup and dependency installation for development
---

## Environment Setup

### Prerequisites

- Python 3.10+ required
- uv package manager

### Creating Virtual Environment

```bash
uv venv
```

### Installing Dependencies

```bash
uv sync --all-extras
```

Or using Makefile:

```bash
make install
```

### Verify Setup

Run tests to verify the environment is correctly configured:

```bash
make quick-test
```

### Common Environment Issues

If tests fail to import the module, ensure the package is installed:

```bash
uv sync
```

If linting tools are not found, reinstall dev dependencies:

```bash
uv sync --all-extras
```
