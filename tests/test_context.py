import re

import pytest
from sphinx_clarity_theme.context import LAYOUTS, get_layout, show_header_menu


def test_show_header_menu():
    assert not show_header_menu({})
    assert not show_header_menu({"header_menu": []})
    assert show_header_menu({"header_menu": [{"content": "Home", "url": "/"}]})


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
