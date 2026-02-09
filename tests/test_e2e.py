import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="insert-tracking-codes")
def test_insert_tracking_codes(app: SphinxTestApp, status, warning):
    app.build()

    assert app.statuscode == 0
    assert (
        '<meta name="head_tag_end" content="foo" />'
        in (app.outdir / "index.html").read_text()
    )
    assert (
        '<meta name="body_tag_end" content="foo" />'
        in (app.outdir / "index.html").read_text()
    )
