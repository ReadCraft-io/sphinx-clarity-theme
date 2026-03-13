from sphinx_clarity_theme import ThemeOptions

project = html_title = "Clarity Theme for Sphinx"
author = "ReadCraft.io"
copyright = f"%Y, {author}"

extensions = [
    # builtin
    # "sphinx.ext.todo",
    # "sphinx.ext.intersphinx",
    # 3rd party
    "myst_parser",
    "sphinx_design",
    # "sphinxcontrib.mermaid",
    "sphinx_reredirects",
    # "sphinx_sitemap",
    "sphinx_copybutton",
    # "ablog",
    "sphinxcontrib.video",
    # "sphinxext.opengraph",
]

templates_path = ["_templates"]

html_theme = "sphinx_clarity_theme"

html_logo = "_static/favicon.svg"
html_favicon = "_static/favicon.svg"
# html_show_sourcelink = False

html_theme_options: ThemeOptions = {
    "logo_dark": "_static/favicon.svg",
    "logo_url": "https://readcraft.io",
    # "edit_page_label": "Edit page on GitHub",
    # "edit_page_url": "https://github.com/documatt/readcraft/edit/main/testdocs/sphinx-clarity-theme/{filename}",
    # https://github.com/documatt/readcraft/edit/main/testdocs/sphinx-clarity-theme/howtos.md
    # "language_select": {
    #     "en": "English",
    #     "cs": "čeština",
    #     "ua": "Українська",
    # },
    # "language_url": "sphinx-clarity-theme/docs/$LANGUAGE$/latest/$PAGE$",
    # "header_menu": [
    #     {
    #         "content": "Getting Started",
    #         "url": "some/url",
    #     },
    #     {
    #         "content": "Pricing ",
    #         "url": "some/url",
    #     },
    #     {
    #         "content": "Resources",
    #         "url": "some/url",
    #     },
    #     {
    #         "content": """Download <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M8 3v8"/><path d="M3.5 8.5L8 13l4.5-4.5"/></svg>""",
    #         "url": "some/url",
    #         "as": "button",
    #     },
    # ],
}
html_static_path = ["_static"]

highlight_language = "none"

html_permalinks_icon = "#"

# -- Options for Markdown ----------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "attrs_inline",
    "attrs_block",
    "deflist",
    "tasklist",
    "linkify",
    "substitution",
    "html_image",
    "colon_fence",
    "strikethrough",
]

myst_substitutions = {
    "project": project,
    "author": author,
    "theme_url": "https://readcraft.io/sphinx-clarity-theme/",
}

# Auto-generated heading anchors
# Allows
#       See settings's [HOME option](../ref/settings.md#HOME).
myst_heading_anchors = 6

# Linky only those that begin with a schema (http://, etc.). Now `documatt.com` will not be converted to a link.
myst_linkify_fuzzy_links = False

# -- Options for Sphinx Redirects ----------------------------------------------------
redirects = {
    "customize/language-selection": "../language-select/",
}
