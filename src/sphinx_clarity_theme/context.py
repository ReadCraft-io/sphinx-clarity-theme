"""Various context helper functions for the Clarity Sphinx theme."""

from typing import Any

from bs4 import BeautifulSoup
from sphinx.application import Sphinx

DEFAULT_LAYOUT = "default"
LAYOUTS = [DEFAULT_LAYOUT, "compact"]


def render_header_menu(header_menu):
    """Render header menu items as HTML list items."""
    soup = BeautifulSoup("", "html.parser")
    result = []

    for item in header_menu:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=item["url"])

        if item.get("as") == "button":
            a["class"] = "btn btn-primary"
            a["role"] = "button"

        # Parse label as HTML to preserve any tags like <svg>
        a.append(BeautifulSoup(item["label"], "html.parser"))

        li.append(a)
        result.append(str(li))

    return "\n".join(result)


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
