from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session


def main():
    config = load_config()

    print("--- Sync Device Time ---")
    missing = set(("ip", "user", "password", "port")).difference(config)
    if missing:
        print(f"Missing credentials: {', '.join(missing)}")
        return 1

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        print("Syncing device time...")
        session.sync_device_time()
        ver = session.verify_device_time()
        print(f"✅ Device time synced (diff={ver['difference_seconds']}s)")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
