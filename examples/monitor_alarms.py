import json
import sys
import logging
from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session

# Configure logging to see what happens
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main() -> int:
    config = load_config()

    print("--- Manual Alarm Monitor ---")
    missing = [k for k in ("ip", "user", "password", "port") if not config.get(k)]
    if missing:
        print(f"Missing credentials: {', '.join(missing)}")
        return 1

    def on_event(lCommand, pAlarmer, pAlarmInfo, pUser):
        # This function is called every time an event arrives
        payload = {
            "lCommand": lCommand,
            "pUser": pUser,
            # You could expand pAlarmer/pAlarmInfo here if you want to inspect them
            "info": "Event received (see logs for full details if expansion is implemented)"
        }
        
        # Pretty print to console
        print(f"\n[EVENT RECEIVED] {json.dumps(payload, indent=2)}")

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        session.start_alarm_channel(
            subscribe_xml=Session.build_subscribe_all_events_xml(),
            by_level=1,
            by_alarm_info_type=1,
            on_event=on_event,
        )

        print("📡 Listening for events... (Press Ctrl+C to stop)")
        try:
            # duration_s=None makes it listen forever
            session.listen_alarm_events(duration_s=None)
        except KeyboardInterrupt:
            print("\n🛑 Stopping...")
        finally:
            session.stop_alarm_channel()
            session.logout()

    return 0

if __name__ == "__main__":
    sys.exit(main())
