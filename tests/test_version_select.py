import re
from unittest.mock import patch

import pytest
from sphinx_clarity_theme.version_select import (
    REQUIRED,
    VERSION_SELECT_CURRENT,
    VERSION_SELECT_DATA,
    VERSION_SELECT_URL,
    show_version_select,
    validate_version_select,
)


def test_show_version_select():
    assert not show_version_select({})
    assert not show_version_select({VERSION_SELECT_CURRENT: "1.0"})
    assert not show_version_select({VERSION_SELECT_DATA: []})
    assert not show_version_select({VERSION_SELECT_URL: "1.0"})
    assert show_version_select(
        {
            VERSION_SELECT_CURRENT: "1.0",
            VERSION_SELECT_URL: "/docs/{version}/",
            VERSION_SELECT_DATA: [
                {"version": "1.0", "label": "1.0 (latest)"},
                {"version": "0.9", "label": "0.9"},
            ],
        }
    )


class TestValidateVersionSelect:
    def test_not_present(self):
        # Options not present - should not raise
        validate_version_select({})

    def test_only_current(self):
        # Only current version provided - should raise
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"If any of the version select options ({', '.join(REQUIRED)}) are provided, all must be provided. Missing: {', '.join([VERSION_SELECT_DATA, VERSION_SELECT_URL])}"
            ),
        ):
            validate_version_select({VERSION_SELECT_CURRENT: "1.0"})

    def test_only_data(self):
        # Only data provided - should raise
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"If any of the version select options ({', '.join(REQUIRED)}) are provided, all must be provided. Missing: {', '.join([VERSION_SELECT_CURRENT, VERSION_SELECT_URL])}"
            ),
        ):
            validate_version_select({VERSION_SELECT_DATA: [{"version": "1.0"}]})

    def test_only_url(self):
        # Only URL provided - should raise
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"If any of the version select options ({', '.join(REQUIRED)}) are provided, all must be provided. Missing: {', '.join([VERSION_SELECT_DATA, VERSION_SELECT_CURRENT])}"
            ),
        ):
            validate_version_select({VERSION_SELECT_URL: "/docs/{version}/"})

    def test_valid(self):
        # Valid options - should not raise
        validate_version_select(
            {
                VERSION_SELECT_CURRENT: "1.0",
                VERSION_SELECT_DATA: [
                    {"version": "1.0"},
                    {"version": "0.9"},
                ],
                VERSION_SELECT_URL: "/docs/{version}/",
            }
        )

    def test_non_dict_option(self):
        # Invalid options - non-dict item
        with pytest.raises(
            ValueError,
            match=f"The '{VERSION_SELECT_DATA}' option must be a dictionary.",
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: ["not a dict"],  # pyright: ignore[reportArgumentType]
                    VERSION_SELECT_URL: "/docs/{version}/",
                }
            )

    def test_missing_url_placeholder(self):
        # Missing 'url' key
        with pytest.raises(
            ValueError,
            match=f"The '{VERSION_SELECT_URL}' option must contain the '{{version}}' placeholder.",
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: [{"version": "1.0"}],  # pyright: ignore[reportArgumentType]
                    VERSION_SELECT_URL: "/docs/version/",  # not "{version}"
                }
            )

    def test_missing_version(self):
        # Missing 'version' key
        with pytest.raises(
            ValueError,
            match=f"Each '{VERSION_SELECT_DATA}' option item must have 'version' key.",
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: [{"url": "/docs/1.0/"}],  # pyright: ignore[reportArgumentType]
                    VERSION_SELECT_URL: "/docs/{version}/",
                }
            )

    def test_setup_calls_validate_version_select(self):
        """Test that setup calls validate_version_select with the theme options."""
        with patch("sphinx_clarity_theme.validate_version_select") as mock_validate:
            from sphinx_clarity_theme import setup

            # Create a mock Sphinx app with config
            class MockConfig:
                html_theme_options = {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: [{"version": "1.0", "url": "/docs/1.0/"}],
                }

            class MockApp:
                config = MockConfig()

                def add_html_theme(self, name, path):
                    pass

                def connect(self, event, callback):
                    pass

            mock_app = MockApp()
            setup(mock_app)  # pyright: ignore[reportArgumentType]

            mock_validate.assert_called_once_with(mock_app.config.html_theme_options)

    def test_current_doesnt_correspond_to_any_version(self):
        """Test that validation fails if the current version doesn't match any of the VERSION_SELECT_DATA versions."""
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"The '{VERSION_SELECT_CURRENT}' version (3.0) doesn't exist in '{VERSION_SELECT_DATA}' versions."
            ),
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "3.0",
                    VERSION_SELECT_DATA: [{"version": "1.0"}, {"version": "0.9"}],
                    VERSION_SELECT_URL: "/docs/{version}/",
                }
            )
