# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

try:
    import sphinx_no_pragma

    version = sphinx_no_pragma.__version__
    project = sphinx_no_pragma.__title__
    copyright = sphinx_no_pragma.__copyright__
    author = sphinx_no_pragma.__author__
except ImportError:
    version = "0.1"
    project = "sphinx-no-pragma"
    copyright = "2023-2025, Artur Barseghyan <artur.barseghyan@gmail.com>"
    author = "Artur Barseghyan <artur.barseghyan@gmail.com>"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_no_pragma",  # Important
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

release = version

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
}

pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
# html_extra_path = ["examples"]

prismjs_base = "//cdnjs.cloudflare.com/ajax/libs/prism/1.29.0"

html_css_files = [
    f"{prismjs_base}/themes/prism.min.css",
    f"{prismjs_base}/plugins/toolbar/prism-toolbar.min.css",
    "https://cdn.jsdelivr.net/gh/barseghyanartur/jsphinx@1.3.4/src/css/sphinx_rtd_theme.css",
]

html_js_files = [
    f"{prismjs_base}/prism.min.js",
    f"{prismjs_base}/plugins/autoloader/prism-autoloader.min.js",
    f"{prismjs_base}/plugins/toolbar/prism-toolbar.min.js",
    f"{prismjs_base}/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js",
    "https://cdn.jsdelivr.net/gh/barseghyanartur/jsphinx/src/js/download_adapter.js",
]

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- sphinx-no-pragma configuration ------------------------------------------
# Override the default endings
# ignore_comments_endings = [
#     "# type: ignore",
#     "# noqa",
#     "# pragma: no cover",
#     "# pragma: no branch",
#     "# fmt: off",
#     "# fmt: on",
#     "# fmt: skip",
#     "# yapf: disable",
#     "# yapf: enable",
#     "# pylint: disable",
#     "# pylint: enable",
#     "# flake8: noqa",
#     "# noinspection",
#     "# pragma: allowlist secret",
#     "# pragma: NOSONAR",
# ]
# Set user defined endings
user_ignore_comments_endings = ["# [start]"]
