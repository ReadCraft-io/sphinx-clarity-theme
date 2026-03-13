from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture(scope="session")
def rootdir():
    return Path(__file__).parent.absolute() / "roots"


def soup(html: str) -> BeautifulSoup:
    """Create a BeautifulSoup object from HTML string."""
    return BeautifulSoup(html, "html.parser")
