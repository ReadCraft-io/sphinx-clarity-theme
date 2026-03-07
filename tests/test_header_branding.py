"""Header title and logo tests."""

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


def soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


@pytest.mark.sphinx(
    "html", testroot="header-branding", confoverrides={"html_title": "Foo"}
)
def test_header_title_same_as_html_title(app: SphinxTestApp):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "index.html").read_text()
    el = soup(html).select_one(".header-branding")
    assert el

    expected = """<a class="header-branding flex items-center gap-4" href="#"><span class="header-branding__title text-primary-content text-2xl font-normal whitespace-nowrap">Foo</span></a>"""

    assert el.prettify() == soup(expected).prettify()


@pytest.mark.sphinx(
    "html",
    testroot="header-branding",
    confoverrides={"html_title": "Foo", "html_theme_options": {"header_title": "Bar"}},
)
def test_custom_header_title(app: SphinxTestApp):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "index.html").read_text()
    el = soup(html).select_one(".header-branding")
    assert el

    expected = """<a class="header-branding flex items-center gap-4" href="#"><span class="header-branding__title text-primary-content text-2xl font-normal whitespace-nowrap">Bar</span></a>"""

    assert el.prettify() == soup(expected).prettify()


@pytest.mark.sphinx(
    "html",
    testroot="header-branding",
    confoverrides={"html_title": "Foo", "html_theme_options": {"header_title": False}},
)
def test_disable_header_title(app: SphinxTestApp):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "index.html").read_text()
    el = soup(html).select_one(".header-branding")
    assert el

    expected = """<a class="header-branding flex items-center gap-4" href="#"></a>"""

    assert el.prettify() == soup(expected).prettify()
