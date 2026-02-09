from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def rootdir():
    return Path(__file__).parent.absolute() / "roots"
