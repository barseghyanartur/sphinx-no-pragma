================
sphinx-no-pragma
================
.. External references

.. _Sphinx: https://github.com/sphinx-doc/sphinx

.. Internal references

.. _sphinx-no-pragma: https://github.com/barseghyanartur/sphinx-no-pragma/
.. _Read the Docs: http://sphinx-no-pragma.readthedocs.io/
.. _Contributor guidelines: https://sphinx-no-pragma.readthedocs.io/en/latest/contributor_guidelines.html

Minimalistic, standalone alternative fake data generator with no dependencies.

.. image:: https://img.shields.io/pypi/v/sphinx-no-pragma.svg
   :target: https://pypi.python.org/pypi/sphinx-no-pragma.py
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/sphinx-no-pragma.svg
    :target: https://pypi.python.org/pypi/sphinx-no-pragma/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/sphinx-no-pragma/actions/workflows/test.yml/badge.svg?branch=main
   :target: https://github.com/barseghyanartur/sphinx-no-pragma/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/sphinx-no-pragma/badge/?version=latest
    :target: http://sphinx-no-pragma.readthedocs.io
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/sphinx-no-pragma/#License
   :alt: MIT

.. image:: https://coveralls.io/repos/github/barseghyanartur/sphinx-no-pragma/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/barseghyanartur/sphinx-no-pragma?branch=main
    :alt: Coverage

`sphinx-no-pragma`_ is a standalone, portable `Sphinx`_ extension for
stripping pragma comments from source code used in documentation.

Written by lazy developer for lazy developers to improve developer experience
and write low-maintenance code.

Features
========
- Accurately stips out pragma comments from your source code that you include
  in your documentation.

Prerequisites
=============
Python 3.8+

Installation
============
pip
---

.. code-block:: sh

    pip install sphinx-no-pragma

Download and copy
-----------------
``sphinx_no_pragma.py`` is the sole, self-contained module of the package.
It includes tests too. If it's more convenient to you, you could simply
download the ``sphinx_no_pragma.py`` module and include it in your repository.

Since tests are included, it won't have a negative impact on your test
coverage (you might need to apply tweaks to your coverage configuration).

Documentation
=============
- Documentation is available on `Read the Docs`_.
- For guidelines on contributing check the `Contributor guidelines`_.

Usage
=====


Tests
=====

Run the tests with unittest:

.. code-block:: sh

    python -m unittest sphinx_no_pragma.py

Or pytest:

.. code-block:: sh

    pytest

License
=======

MIT

Support
=======
For security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to
`GitHub <https://github.com/barseghyanartur/sphinx-no-pragma/issues>`_.

Author
======

Artur Barseghyan <artur.barseghyan@gmail.com>
