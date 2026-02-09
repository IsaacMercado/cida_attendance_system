import os

import pytest

from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session


# Allows tests to be skipped if no configuration is present
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: mark test as requiring hardware connection",
    )


@pytest.fixture(scope="session")
def sdk_config():
    """Loads configuration. If missing, skips integration tests."""
    config = load_config()
    required = ["ip", "user", "password"]

    # Check if minimum keys are present
    if any(not config.get(k) for k in required):
        if os.getenv("CI"):
            pytest.fail("Missing credentials in CI environment")
        else:
            pytest.skip("Missing configuration in ~/.config/cida_attendance/config.ini")

    return config


@pytest.fixture(scope="function")
def session(sdk_config):
    """Provides a logged-in SDK session and cleans it up upon completion."""
    sess = Session()
    sess.init()  # Initialize SDK before login
    if not sess.login(**sdk_config):
        pytest.fail("Could not log in to the device (Login Failed)")

    yield sess

    sess.logout()
    sess.cleanup()
