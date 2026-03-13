from typing import Literal, NotRequired, Sequence, TypedDict

DEFAULT_LAYOUT = "default"
LAYOUTS = [DEFAULT_LAYOUT, "compact"]

# Nice TypedDict class syntax cannot be used due to collision of key names with Python reserved keywords (e.g. "as", etc.)

HeaderMenuItem = TypedDict(
    "HeaderMenuItem",
    {
        "content": str,
        "url": str,
        "as": NotRequired[Literal["button"]],
        "tooltip": NotRequired[str],
    },
)

HeaderMenu = Sequence[HeaderMenuItem]

VersionSelectDataItem = TypedDict(
    "VersionSelectDataItem",
    {"version": str, "label": NotRequired[str]},
)

VersionSelectData = Sequence[VersionSelectDataItem]


ThemeOptions = TypedDict(
    "ThemeOptions",
    {
        "default_layout": str,
        "header_title": str | Literal[False],
        "header_menu": HeaderMenu,
        "logo_url": str,
        "logo_dark": str,
        "logo_dark_invert": bool,
        "language_select": dict[str, str],
        "language_url": str,
        "edit_page_label": str,
        "edit_page_url": str,
        "version_select_current": str,
        "version_select_data": VersionSelectData,
        "version_select_url": str,
        "version_select_preferred": str,
        "version_select_preferred_warning": str,
        "announcement": str,
    },
    total=False,
)
