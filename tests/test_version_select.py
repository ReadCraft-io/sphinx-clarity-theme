import re
from unittest.mock import patch

import pytest
from sphinx.testing.util import SphinxTestApp
from sphinx_clarity_theme.version_select import (
    REQUIRED,
    VERSION_SELECT_CURRENT,
    VERSION_SELECT_DATA,
    VERSION_SELECT_PREFERRED,
    VERSION_SELECT_URL,
    VERSION_SELECT_URL_PLACEHOLDER,
    show_version_select,
    validate_version_select,
)

from .conftest import soup


def test_show_version_select():
    assert not show_version_select({})
    assert not show_version_select({VERSION_SELECT_CURRENT: "1.0"})
    assert not show_version_select({VERSION_SELECT_DATA: []})
    assert not show_version_select({VERSION_SELECT_URL: "1.0"})
    assert show_version_select(
        {
            VERSION_SELECT_CURRENT: "1.0",
            VERSION_SELECT_URL: "/docs/$VERSION$/",
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
            validate_version_select({VERSION_SELECT_URL: "/docs/$VERSION$/"})

    def test_valid(self):
        # Valid options - should not raise
        validate_version_select(
            {
                VERSION_SELECT_CURRENT: "1.0",
                VERSION_SELECT_DATA: [
                    {"version": "1.0"},
                    {"version": "0.9"},
                ],
                VERSION_SELECT_URL: "/docs/$VERSION$/",
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
                    VERSION_SELECT_URL: "/docs/$VERSION$/",
                }
            )

    def test_missing_url_placeholder(self):
        # Missing 'url' key
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"The '{VERSION_SELECT_URL}' option must contain the '{VERSION_SELECT_URL_PLACEHOLDER}' placeholder."
            ),
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: [{"version": "1.0"}],  # pyright: ignore[reportArgumentType]
                    VERSION_SELECT_URL: "/docs/version/",  # not "$VERSION$"
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
                    VERSION_SELECT_URL: "/docs/$VERSION$/",
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
                    VERSION_SELECT_URL: "/docs/$VERSION$/",
                }
            )

    def test_preferred_is_not_in_data(self):
        """Test that validation fails if the preferred version doesn't match any of the VERSION_SELECT_DATA versions."""
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"The '{VERSION_SELECT_PREFERRED}' version (2.0) doesn't exist in '{VERSION_SELECT_DATA}' versions."
            ),
        ):
            validate_version_select(
                {
                    VERSION_SELECT_CURRENT: "1.0",
                    VERSION_SELECT_DATA: [{"version": "1.0"}, {"version": "0.9"}],
                    VERSION_SELECT_URL: "/docs/$VERSION$/",
                    VERSION_SELECT_PREFERRED: "2.0",
                }
            )


@pytest.mark.sphinx("html", testroot="version-select-preferred")
def test_version_select__preferred(app: SphinxTestApp, status, warning):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "index.html").read_text()
    el = soup(html).select_one(".version-select")
    assert el

    expected = """
    <div class="version-select">
        <div class="tooltip tooltip-bottom" data-tip="Choose a version">
            <select class="select select-ghost select-sm md:select-md m-1" aria-label="Version select">
                <option value="3.0" data-url="/3.0/" selected disabled>3.0</option>
                <option value="2.0" data-url="/2.0/">2.0</option>
                <option value="1.0" data-url="/1.0/">1.0</option>
            </select>
        </div>
    </div>
    """

    assert el.prettify() == soup(expected).prettify()


@pytest.mark.sphinx("html", testroot="version-select-custom-warning")
def test_version_select__custom_warning(app: SphinxTestApp, status, warning):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "index.html").read_text()
    el = soup(html).select_one(".version-select")
    assert el

    expected = """
    <div class="version-select">
        <div class="tooltip tooltip-bottom tooltip-open tooltip-warning">
            <div class="tooltip-content pointer-events-auto">
                <a href="/3.0/"> Hey, the 3.0 is latest version! </a>
            </div>
            <select class="select select-ghost select-sm md:select-md m-1" aria-label="Version select">
                <option value="3.0" data-url="/3.0/">3.0</option>
                <option value="2.0" data-url="/2.0/" selected disabled>2.0</option>
                <option value="1.0" data-url="/1.0/">1.0</option>
            </select>
        </div>
    </div>
    """

    assert el.prettify() == soup(expected).prettify()
