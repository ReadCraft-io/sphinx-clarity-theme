"""A clean and professional documentation theme for Sphinx. Modern design with light/dark mode, responsive layout, and beautiful typography."""

__version__ = "1.0.1post3"

from pathlib import Path
from typing import Any

import docutils
from sphinx.application import Sphinx

from .context import get_layout, render_header_menu

THEME_NAME = "sphinx_clarity_theme"
THEME_HUMAN_NAME = "Clarity Theme for Sphinx"
THEME_URL = "https://readcraft.io/sphinx-clarity-theme/"


def setup(app: Sphinx) -> dict[str, bool]:
    """Setup the Sphinx application."""
    theme_path = str(Path(__file__).parent.resolve())
    app.add_html_theme(THEME_NAME, theme_path)

    app.connect("html-page-context", register_to_context)

    return {"parallel_read_safe": True, "parallel_write_safe": True}


def register_to_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: docutils.nodes.document | None,
):
    # Add it to the page's context
    context["header_menu"] = lambda: render_header_menu(
        app.config.html_theme_options.get("header_menu", [])
    )
    context["theme_version"] = __version__
    context["theme_name"] = THEME_NAME
    context["theme_human_name"] = THEME_HUMAN_NAME
    context["theme_url"] = THEME_URL
    context["get_layout"] = lambda: get_layout(app, context)
