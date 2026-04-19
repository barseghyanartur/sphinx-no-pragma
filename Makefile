.PHONY: build test test-env shell shell-env quick-test ipython \
        doc8 ruff mypy clean-dev clean-test clean pre-commit

VERSION := 0.1.3
SHELL := /bin/bash
# Makefile for project
VENV := .venv/bin/activate
UNAME_S := $(shell uname -s)

# -----------------------------------------------------------------------
# Build and testing (Docker-based)
# -----------------------------------------------------------------------

build:
	docker compose build

test: build
	docker compose run --rm tox

test-env: build
	@if [ -z "$(ENV)" ]; then \
		echo "Usage: make test-env ENV=py312"; \
		exit 1; \
	fi
	docker compose run --rm tox -e $(ENV)

shell: build
	docker compose run --rm --entrypoint bash tox

shell-env: build
	@if [ -z "$(ENV)" ]; then \
		echo "Usage: make shell-env ENV=py312"; \
		exit 1; \
	fi
	docker compose run --rm --entrypoint bash tox -e $(ENV)

# -----------------------------------------------------------------------
# uv-based testing (run locally)
# -----------------------------------------------------------------------

quick-test:
	uv run pytest

ipython:
	uv run ipython

# -----------------------------------------------------------------------
# Code quality
# -----------------------------------------------------------------------

doc8:
	uv run doc8

ruff:
	uv run ruff check . --fix
	uv run ruff format .

mypy:
	uv run mypy sphinx_no_pragma.py

# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------

# Build documentation using Sphinx and zip it
build-docs:
	uv run sphinx-source-tree
	uv run sphinx-build -n -b text docs builddocs
	uv run sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

rebuild-docs:
	uv run sphinx-apidoc . --full -o docs -H 'sphinx-no-pragma' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/index.rst.distrib docs/index.rst
	cp docs/conf.py.distrib docs/conf.py

auto-build-docs:
	uv run sphinx-autobuild docs docs/_build/html --port 5001

# Serve the built docs on port 5001
serve-docs:
	cd builddocs && python -m http.server 5001

compile-requirements:
	uv run uv pip compile --all-extras -o docs/requirements.txt pyproject.toml

compile-requirements-upgrade:
	uv run uv pip compile --all-extras -o docs/requirements.txt pyproject.toml --upgrade

# ----------------------------------------------------------------------------
# Pre-commit
# ----------------------------------------------------------------------------

pre-commit-install:
	pre-commit install

pre-commit: pre-commit-install
	pre-commit run --all-files

# ----------------------------------------------------------------------------
# Installation
# ----------------------------------------------------------------------------

create-venv:
	uv venv

# Install the project
install:
	uv sync --all-extras

# ----------------------------------------------------------------------------
# Security
# ----------------------------------------------------------------------------

scan-secrets:
	uv run detect-secrets scan > .secrets.baseline

verify-secrets:
	uv run detect-secrets scan --baseline .secrets.baseline

# -----------------------------------------------------------------------
# Housekeeping
# -----------------------------------------------------------------------

clean-dev:
	find . -name "*.orig" -exec rm -rf {} +
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf dist/ sphinx_no_pragma.egg-info/ .cache/ .mypy_cache/ .ruff_cache/

clean-test:
	find . -name "*.pyc" -exec rm -rf {} +
	rm -rf .coverage .pytest_cache/ htmlcov/

clean: clean-dev clean-test
	rm -rf builddocs/
	rm -rf test_build_docs/
	rm -rf build/

update-version:
	@echo "Updating version in pyproject.toml and sphinx_no_pragma.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' sphinx_no_pragma.py; \
	else \
		sed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' sphinx_no_pragma.py; \
	fi

# ----------------------------------------------------------------------------
# Release
# ----------------------------------------------------------------------------

package-build:
	uv run python -m build .

check-package-build:
	uv run twine check dist/*

release:
	uv run twine upload dist/* --verbose

test-release:
	uv run twine upload --repository testpypi dist/* --verbose

# ----------------------------------------------------------------------------
# Other
# ----------------------------------------------------------------------------

%:
	@:
