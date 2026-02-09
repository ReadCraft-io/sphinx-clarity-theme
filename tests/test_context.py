import re

import pytest
from bs4 import BeautifulSoup
from sphinx_clarity_theme.context import LAYOUTS, get_layout, render_header_menu


class TestRenderHeaderMenu:
    def test_render_header_menu(self):
        header_menu = [
            {
                "label": "Getting Started",
                "url": "some/url",
            },
            {
                "label": "Pricing",
                "url": "some/url",
            },
            {
                "label": 'Download <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 1em;"><polyline points="6 9 12 15 18 9"/></svg>',
                "url": "some/url",
                "as": "button",
            },
        ]

        expected = """
        <li><a href="some/url">Getting Started</a></li>
        <li><a href="some/url">Pricing</a></li>
        <li>
        <a class="btn btn-primary" href="some/url" role="button">
            Download
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 1em;"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        </li>"""

        output = render_header_menu(header_menu)

        assert (
            BeautifulSoup(output, "html.parser").prettify()
            == BeautifulSoup(expected, "html.parser").prettify()
        )

    def test_render_header_menu_empty(self):
        header_menu = []
        output = render_header_menu(header_menu)
        assert output == ""


class TestGetLayout:
    def test_get_layout_no_meta(self):
        """If no layout is set in page meta, use global html_theme_options layout."""

        class DummyApp:
            config = type(
                "Config", (), {"html_theme_options": {"default_layout": "compact"}}
            )()

        context = {}

        layout = get_layout(DummyApp(), context)  # pyright: ignore[reportArgumentType]

        assert layout == "compact"

    def test_get_layout_with_meta(self):
        """If layout is set in both page meta and global html_theme_options, use meta value."""

        class DummyApp:
            config = type(
                "Config", (), {"html_theme_options": {"default_layout": "default"}}
            )()

        context = {"meta": {"layout": "compact"}}

        layout = get_layout(DummyApp(), context)  # pyright: ignore[reportArgumentType]

        assert layout == "compact"

    def test_get_layout_global_raise_invalid_layout(self):
        """Raise ValueError if html_theme_options layout is invalid."""

        class DummyApp:
            config = type(
                "Config", (), {"html_theme_options": {"default_layout": "invalid"}}
            )()

        context = {}

        expected_message = f"The html_theme_options 'default_layout' has invalid value 'invalid'. Allowed values are {LAYOUTS}."
        with pytest.raises(ValueError, match=re.escape(expected_message)):
            get_layout(DummyApp(), context)  # pyright: ignore[reportArgumentType]

    def test_get_layout_page_raise_invalid_layout(self):
        """Raise ValueError if page meta layout is invalid."""

        class DummyApp:
            config = type("Config", (), {"html_theme_options": {}})()

        context = {"meta": {"layout": "wide"}}

        expected_message = f"The page meta 'layout' option has invalid value 'wide'. Allowed values are {LAYOUTS}."
        with pytest.raises(ValueError, match=re.escape(expected_message)):
            get_layout(DummyApp(), context)  # pyright: ignore[reportArgumentType]
