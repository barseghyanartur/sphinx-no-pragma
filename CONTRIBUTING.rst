Contributor guidelines
======================

.. _documentation: https://sphinx-no-pragma.readthedocs.io/#writing-documentation
.. _testing: https://sphinx-no-pragma.readthedocs.io/#testing
.. _pre-commit: https://pre-commit.com/#installation
.. _black: https://black.readthedocs.io/
.. _isort: https://pycqa.github.io/isort/
.. _doc8: https://doc8.readthedocs.io/
.. _ruff: https://beta.ruff.rs/docs/
.. _pip-tools: https://pip-tools.readthedocs.io/
.. _issues: https://github.com/barseghyanartur/sphinx-no-pragma/issues
.. _discussions: https://github.com/barseghyanartur/sphinx-no-pragma/discussions
.. _pull request: https://github.com/barseghyanartur/sphinx-no-pragma/pulls
.. _support: https://sphinx-no-pragma.readthedocs.io/#support
.. _installation: https://sphinx-no-pragma.readthedocs.io/#installation
.. _features: https://sphinx-no-pragma.readthedocs.io/#features
.. _prerequisites: https://sphinx-no-pragma.readthedocs.io/#prerequisites
.. _demo: https://sphinx-no-pragma.readthedocs.io/en/latest/demo.html

Developer prerequisites
-----------------------
pre-commit
~~~~~~~~~~
Refer to `pre-commit`_ for installation instructions.

TL;DR:

.. code-block:: sh

    pip install pipx --user  # Install pipx
    pipx install pre-commit  # Install pre-commit
    pre-commit install  # Install pre-commit hooks

Installing `pre-commit`_ will ensure you adhere to the project code quality
standards.

Code standards
--------------
`black`_, `isort`_, `ruff`_ and `doc8`_ will be automatically triggered by
`pre-commit`_. Still, if you want to run checks manually:

.. code-block:: sh

    make black
    make doc8
    make isort
    make ruff

Requirements
------------
Requirements are compiled using `pip-tools`_.

.. code-block:: sh

    make compile-requirements

Virtual environment
-------------------
You are advised to work in virtual environment.

TL;DR:

.. code-block:: sh

    python -m venv env
    pip install -e .[all]

Documentation
-------------
Check `documentation`_.

Testing
-------
Check `testing`_.

If you introduce changes or fixes, make sure to test them locally using
all supported environments. For that use tox.

.. code-block:: sh

    tox

In any case, GitHub Actions will catch potential errors, but using tox speeds
things up.

Pull requests
-------------
You can contribute to the project by making a `pull request`_.

For example:

- To fix documentation typos.
- To improve documentation (for instance, to add new rule or fix
  an existing rule that doesn't seem to work).
- To introduce a new feature.

**General list to go through:**

- Does your change require documentation update?
- Does your change require update to tests?

**When fixing bugs (in addition to the general list):**

- Make sure to add regression tests.

**When adding a new feature (in addition to the general list):**

- Make sure to update the documentation (check whether the `installation`_,
  `features`_ or `demo`_ require changes).

Questions
---------
Questions can be asked on GitHub `discussions`_.

Issues
------
For reporting a bug or filing a feature request use GitHub `issues`_.

**Do not report security issues on GitHub**. Check the `support`_ section.
