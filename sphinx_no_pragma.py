"""
https://github.com/barseghyanartur/sphinx-no-pragma/
"""

from docutils import nodes
from sphinx.directives.code import LiteralInclude
from tests import TestNoPragmaLiteralInclude
__title__ = "sphinx-no-pragma"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "NoPragmaLiteralInclude",
    "setup",
)


class NoPragmaLiteralInclude(LiteralInclude):
    def run(self):
        # Retrieve the global configuration set in conf.py
        ignore_endings = (
            self.state.document.settings.env.config.ignore_comments_endings
        )
        if not isinstance(ignore_endings, list):
            ignore_endings = [ignore_endings]

        # Get the original content generated by LiteralInclude
        original_content = super().run()
        new_content = []

        for node in original_content:
            if isinstance(node, nodes.literal_block):
                # Modify lines by removing specified endings
                lines = node.rawsource.splitlines()
                filtered_lines = [
                    self.remove_endings(line, ignore_endings) for line in lines
                ]

                # Update the node content
                node.rawsource = "\n".join(filtered_lines)
                node[:] = [nodes.Text("\n".join(filtered_lines))]
            new_content.append(node)

        return new_content

    def remove_endings(self, line, endings):
        # Remove specified endings from a line
        for ending in endings:
            if line.endswith(ending):
                return line[: -len(ending)].rstrip()
        return line


def setup(app):
    app.add_directive("literalinclude", NoPragmaLiteralInclude, override=True)
    app.add_config_value(
        "ignore_comments_endings", ["# type: ignore", "# noqa"], "env"
    )

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
