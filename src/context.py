"""Various context helper functions for the Clarity Sphinx theme."""

from typing import Any

from sphinx.application import Sphinx

from .options import DEFAULT_LAYOUT, LAYOUTS, ThemeOptions


def show_header_menu(options: ThemeOptions) -> bool:
    """Determine whether the header menu should be shown on the current page."""
    return bool(options.get("header_menu"))


def get_layout(app: Sphinx, context: dict[str, Any]) -> str:
    """
    Determine the layout to use for the current page. Either a page-specific layout or the theme's default layout.
    """
    layout = None

    # *** Page meta layout ***
    if context.get("meta") and context["meta"].get("layout"):
        layout = context["meta"]["layout"]

    if layout and layout not in LAYOUTS:
        raise ValueError(
            f"The page meta 'layout' option has invalid value '{layout}'. Allowed values are {LAYOUTS}."
        )

    if layout:
        return layout

    # *** Global layout ***
    layout = app.config.html_theme_options.get("default_layout")

    # If no layout is specified in theme options, use the default layout
    if layout and layout not in LAYOUTS:
        raise ValueError(
            f"The html_theme_options 'default_layout' has invalid value '{layout}'. Allowed values are {LAYOUTS}."
        )

    if not layout:
        layout = DEFAULT_LAYOUT

    return layout
