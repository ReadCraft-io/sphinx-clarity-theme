# Common issues

Frequent configuration mistakes and their fixes when using {{ project }} and Sphinx.

## WARNING: unsupported theme option 'xyz' given

Sphinx found an unknown option in `html_theme_options` (usually a misspelling). See [](#reference-html-theme-options) for the complete list.

Incorrect:

```py
html_theme_options = {
    "defaultlayout": "compact",  # wrong key
}
```

Correct:

```py
html_theme_options = {
    "default_layout": "compact",  # correct key
}
```

## IsADirectoryError

Build fails with an error similar to:

```
sphinx.errors.ThemeError: An error happened in rendering the page index.
    Reason: IsADirectoryError(21, 'Is a directory')
```

Cause: `html_css_files` (or `html_js_files`) is a single string instead of a list.

Incorrect:

```py
html_css_files = "styles/custom.css"
```

Correct:

```py
html_css_files = ["styles/custom.css"]
```
