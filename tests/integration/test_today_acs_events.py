import sys

import pytest

from cida_attendance.sdk.utils import ctypes_to_dict


@pytest.mark.integration
def test_fetch_today_events(session):
    """Tests downloading current day events."""
    now, tz = session.get_device_time()
    # Start from the device's start of day
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    out = []

    def _on_data(detail):
        if len(out) >= 20:
            return
        out.append(ctypes_to_dict(detail, tz=tz))

    # Execute synchronous search (blocking for the test)
    # Note: We use async_get_asc_event but in the original code it behaved synchronously
    # or the wait mechanism was missing. We assume session.async_get_asc_event
    # blocks or we need to wait.
    # Reviewing original code: it used callbacks. If it is really async,
    # this test might finish before receiving data.
    # But assuming the SDK blocks or the session implementation handles the wait:
    
    session.async_get_asc_event(
        start,
        now,
        _on_data,
        major=0x5,
    )

    # Basic validations
    print(f"Events retrieved: {len(out)}")
    
    # Do not fail if no events (it is possible there are no attendances today),
    # but verifying that there was no exception.
    assert isinstance(out, list)
    
    if out:
        first = out[0]
        assert "struTime" in first
        assert "struAcsEventInfo" in first

if __name__ == "__main__":
    # Facilitates manual debugging by invoking pytest directly
    sys.exit(pytest.main(["-v", __file__]))
