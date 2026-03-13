from .options import ThemeOptions

VERSION_SELECT_DATA = "version_select_data"
VERSION_SELECT_CURRENT = "version_select_current"
VERSION_SELECT_URL = "version_select_url"
VERSION_SELECT_URL_PLACEHOLDER = "$VERSION$"
VERSION_SELECT_PREFERRED = "version_select_preferred"

REQUIRED = (VERSION_SELECT_DATA, VERSION_SELECT_CURRENT, VERSION_SELECT_URL)


def validate_version_select(options: ThemeOptions):
    """Validate the version select options in the theme options."""
    # Quit if no version select options are present
    if not any(key in options for key in REQUIRED):
        return

    # If any of the required options are present, all must be present
    if any(key in options for key in REQUIRED) and not all(
        key in options for key in REQUIRED
    ):
        missing = [key for key in REQUIRED if key not in options]
        raise ValueError(
            f"If any of the version select options ({', '.join(REQUIRED)}) are provided, all must be provided. Missing: {', '.join(missing)}"
        )

    # Validate data
    assert VERSION_SELECT_DATA in options
    for option in options[VERSION_SELECT_DATA]:  # type: ignore[literal-required]
        if not isinstance(option, dict):
            raise ValueError(
                f"The '{VERSION_SELECT_DATA}' option must be a dictionary."
            )
        if "version" not in option:
            raise ValueError(
                f"Each '{VERSION_SELECT_DATA}' option item must have 'version' key."
            )

    # Validate URL contains version placeholder
    assert VERSION_SELECT_URL in options
    if VERSION_SELECT_URL_PLACEHOLDER not in options[VERSION_SELECT_URL]:  # type: ignore[literal-required]
        raise ValueError(
            f"The '{VERSION_SELECT_URL}' option must contain the '{VERSION_SELECT_URL_PLACEHOLDER}' placeholder."
        )

    # Ensure the current version matches one of the data versions
    assert VERSION_SELECT_CURRENT in options
    current_version = options[VERSION_SELECT_CURRENT]  # type: ignore[literal-required]
    if not any(
        option["version"] == current_version
        for option in options[VERSION_SELECT_DATA]  # type: ignore[literal-required]
    ):
        raise ValueError(
            f"The '{VERSION_SELECT_CURRENT}' version ({current_version}) doesn't exist in '{VERSION_SELECT_DATA}' versions."
        )

    # If preferred version is set, ensure it matches one of the data versions
    if VERSION_SELECT_PREFERRED in options:
        preferred_version = options[VERSION_SELECT_PREFERRED]  # type: ignore[literal-required]
        if not any(
            option["version"] == preferred_version
            for option in options[VERSION_SELECT_DATA]  # type: ignore[literal-required]
        ):
            raise ValueError(
                f"The '{VERSION_SELECT_PREFERRED}' version ({preferred_version}) doesn't exist in '{VERSION_SELECT_DATA}' versions."
            )


def show_version_select(theme_options: ThemeOptions) -> bool:
    """Determine whether to show the version select in the header."""
    return all(key in theme_options for key in REQUIRED)


def get_version_url(theme_options: ThemeOptions, version: str) -> str:
    """Get the URL for a specific version based on the theme options."""
    assert VERSION_SELECT_URL in theme_options
    template_url = theme_options[VERSION_SELECT_URL]  # type: ignore[literal-required]
    new_url = template_url.replace(VERSION_SELECT_URL_PLACEHOLDER, version)
    return new_url
