#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v nfpm >/dev/null 2>&1; then
  echo "nfpm is required to build .deb/.rpm packages."
  echo "Install options:"
  echo "  - Go:   go install github.com/goreleaser/nfpm/v2/cmd/nfpm@latest"
  echo "  - Or download a release binary from: https://github.com/goreleaser/nfpm"
  exit 2
fi

VERSION="$(uv run python -c "import tomllib, pathlib; p=pathlib.Path('pyproject.toml').read_bytes(); print(tomllib.loads(p)['project']['version'])")"

rm -rf build dist
uv run pyinstaller installers/cida_attendance_headless.spec

# Stage files for nfpm.
rm -rf build/package
mkdir -p build/package/opt
cp -a dist/cida_attendance build/package/opt/cida_attendance

mkdir -p build/package/usr/bin
ln -sf /opt/cida_attendance/cida_attendance build/package/usr/bin/cida_attendance

chmod +x packaging/scripts/postinstall.sh packaging/scripts/preremove.sh

# Build packages.
VERSION="$VERSION" nfpm package -f packaging/nfpm.yaml -p deb -t dist/
VERSION="$VERSION" nfpm package -f packaging/nfpm.yaml -p rpm -t dist/

echo "Built packages in dist/:"
ls -1 dist/*.deb dist/*.rpm 2>/dev/null || true
