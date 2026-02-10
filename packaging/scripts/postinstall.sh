#!/bin/sh
set -e

# Create service user if missing (best-effort; may fail on some systems).
if command -v useradd >/dev/null 2>&1; then
  if ! id -u cida >/dev/null 2>&1; then
    useradd --system --home /opt/cida_attendance --shell /usr/sbin/nologin cida || true
  fi
fi

# Permissions (best-effort).
chown -R cida:cida /opt/cida_attendance 2>/dev/null || true

# Do not auto-enable the service.
exit 0
