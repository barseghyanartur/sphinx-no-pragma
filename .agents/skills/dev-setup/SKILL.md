---
name: dev-setup
description: Environment setup and dependency installation for development
---

## Environment Setup

### Prerequisites

- Python 3.10+ required
- Virtual environment recommended

### Installation

Install the project with all dependencies:

```bash
pip install -e .'[all]'
```

Or using the Makefile:

```bash
make install
```

### Common Environment Issues

If tests fail to import the module, ensure the package is installed in development mode:

```bash
pip install -e .
```

If linting tools are not found, reinstall dev dependencies:

```bash
pip install -e .'[dev]'
```

### Verify Setup

Run tests to verify the environment is correctly configured:

```bash
pytest -vrx -s
```