from sphinx_clarity_theme import ThemeOptions

html_theme = "sphinx_clarity_theme"

html_theme_options: ThemeOptions = {
    "version_select_current": "2.0",
    "version_select_data": [
        {"version": "3.0"},
        {"version": "2.0"},
        {"version": "1.0"},
    ],
    "version_select_url": "/$VERSION$/",
    "version_select_preferred": "3.0",
    "version_select_preferred_warning": "Hey, the $PREFERRED$ is latest version!",
}
