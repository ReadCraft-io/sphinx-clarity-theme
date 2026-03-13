import pytest
from sphinx.testing.util import SphinxTestApp

from .conftest import soup


@pytest.mark.sphinx("html", testroot="announcement")
def test_announcement_rendered(app: SphinxTestApp, status, warning):
    app.build()
    assert app.statuscode == 0

    html = (app.outdir / "foo" / "bar.html").read_text()
    el = soup(html).select_one(".announcement")
    assert el

    expected = """
        <div class="announcement">
          <div class="bg-base-200/25 text-base-content border-base-200 border-b">
            <div
              class="container mx-auto flex items-center justify-between gap-4 px-4 py-2 text-sm"
            >
              <div class="flex flex-1 items-center justify-center gap-2">
                <div class="announcement__content prose prose-sm max-w-none">
                  <strong>Deprecated version!</strong> See this page in the latest  <a href="/stable/foo/bar.html">stable version</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        """
    assert el.prettify() == soup(expected).prettify()
