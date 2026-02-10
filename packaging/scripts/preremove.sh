#!/bin/sh
set -e

# Stop service if running (best-effort).
if command -v systemctl >/dev/null 2>&1; then
  systemctl stop cida-attendance.service >/dev/null 2>&1 || true
  systemctl disable cida-attendance.service >/dev/null 2>&1 || true
fi

exit 0
