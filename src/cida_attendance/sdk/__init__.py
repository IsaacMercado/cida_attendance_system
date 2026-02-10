"""
Full Hikvision SDK

This module contains ALL automatically generated SDK functions.

Usage:
    from cida_attendance.sdk import NET_DVR_Init, NET_DVR_Login_V40
    import cida_attendance.sdk as sdk  # Direct access to all symbols
"""

from __future__ import annotations

import importlib
from types import ModuleType
from typing import Any

_generated: ModuleType | None = None


def _load_generated() -> ModuleType:
    global _generated
    if _generated is None:
        _generated = importlib.import_module("cida_attendance.sdk._generated")
    return _generated


def __getattr__(name: str) -> Any:
    module = _load_generated()
    return getattr(module, name)


def __dir__() -> list[str]:
    base = set(globals().keys())
    try:
        module = _load_generated()
        base.update(dir(module))
    except Exception:
        pass
    return sorted(base)


__all__ = []
