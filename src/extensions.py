from pathlib import Path

from sphinx.application import Sphinx

SPHINX_TABS = "sphinx_tabs.tabs"


def overwrite_extension_assets(app: Sphinx, exception: Exception | None) -> None:
    """Blank out third-party extension CSS files that clash with theme styles.

    Sphinx copies static files in order: theme → extensions, so any shadow
    file inside the theme's static/ directory is overwritten by the extension.
    Running after ``build-finished`` guarantees the theme always wins.
    """
    if exception or app.builder.format != "html":
        return

    def _blankout_file(path: Path) -> None:
        if path.exists():
            path.write_text(
                "/* Intentionally empty — overridden by Clarity Theme for Sphinx */\n"
            )

    if SPHINX_TABS in app.extensions:
        _blankout_file(Path(app.outdir) / "_static" / "tabs.css")


def add_extension_assets(app: Sphinx) -> None:
    """Conditionally inject CSS for supported third-party extensions.

    Each stylesheet is only added when the corresponding extension is actually
    enabled by the documentation project, so projects that don't use an
    extension pay no loading cost for its styles.
    """
    if SPHINX_TABS in app.extensions:
        app.add_css_file("styles/extensions/sphinx-tabs.css")
