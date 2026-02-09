import pytest

from cida_attendance.sdk.session import Session


@pytest.mark.integration
def test_alarm_subscription(session):
    """Verifies that the alarm channel can be started and stopped without errors."""

    events_received = []

    def on_event(lCommand, pAlarmer, pAlarmInfo, pUser):
        payload = {"lCommand": lCommand, "pUser": pUser}
        events_received.append(payload)
        # In a real scenario, we would log the event here

    # 1. Start alarm channel
    session.start_alarm_channel(
        subscribe_xml=Session.build_subscribe_all_events_xml(),
        by_level=1,
        by_alarm_info_type=1,
        on_event=on_event,
    )

    # 2. Listen for a short period to ensure it doesn't blow up
    # (We cannot guarantee an alarm arrives in 2 seconds, but
    #  we verify that the "listen" mechanism does not throw immediate exception)
    try:
        session.listen_alarm_events(duration_s=2)
    except Exception as e:
        pytest.fail(f"listen_alarm_events failed with exception: {e}")
    finally:
        session.stop_alarm_channel()

    # If we get here without errors, the test passes (smoke test)
    assert True
