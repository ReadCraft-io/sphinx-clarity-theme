"""A clean and professional documentation theme for Sphinx. Modern design with light/dark mode, responsive layout, and beautiful typography."""

__version__ = "2.1.0"

from pathlib import Path
from typing import Any

import docutils
from sphinx.application import Sphinx

from .context import get_layout, show_header_menu
from .extensions import add_extension_assets, overwrite_extension_assets
from .options import (
    HeaderMenuItem,
    ThemeOptions,
    VersionSelectData,
    VersionSelectDataItem,
)
from .version_select import (
    get_version_url,
    show_version_select,
    validate_version_select,
)

__all__ = [
    "HeaderMenuItem",
    "ThemeOptions",
    "VersionSelectData",
    "VersionSelectDataItem",
]

THEME_NAME = "sphinx_clarity_theme"
THEME_HUMAN_NAME = "Clarity Theme for Sphinx"
THEME_URL = "https://readcraft.io/sphinx-clarity-theme/"


def register_to_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: docutils.nodes.document | None,
):
    # Add it to the page's context
    context["theme_version"] = __version__
    context["theme_name"] = THEME_NAME
    context["theme_human_name"] = THEME_HUMAN_NAME
    context["theme_url"] = THEME_URL
    context["get_layout"] = lambda: get_layout(app, context)
    context["show_header_menu"] = lambda: show_header_menu(
        app.config.html_theme_options
    )
    context["show_version_select"] = lambda: show_version_select(
        app.config.html_theme_options
    )
    context["get_version_url"] = lambda version: get_version_url(
        app.config.html_theme_options, version
    )


def setup(app: Sphinx) -> dict[str, bool]:
    """Setup the Sphinx application."""
    theme_path = str(Path(__file__).parent.resolve())
    app.add_html_theme(THEME_NAME, theme_path)

    validate_version_select(app.config.html_theme_options)

    app.connect("html-page-context", register_to_context)
    app.connect("builder-inited", add_extension_assets)
    app.connect("build-finished", overwrite_extension_assets)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
