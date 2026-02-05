"""Compat shim (SDK Hikvision).

Históricamente este proyecto tenía un "loader" propio y bindings parciales.
Ahora se usa el wrapper completo generado por ctypesgen en `cida_attendance.sdk`,
que ya incluye su loader multiplataforma.

Este módulo queda como capa de compatibilidad con helpers básicos.
"""

from __future__ import annotations

import platform
import sys

import cida_attendance.sdk as _sdk

# Re-export: todo el SDK
from cida_attendance.sdk import *  # noqa: F401,F403

# ============================================================================
# Funciones Helper
# ============================================================================


def get_sdk_version():
    """
    Obtiene la versión del SDK

    Returns:
        dict: Información de versión con keys:
            - version: Código de versión (DWORD)
            - build: Número de build
            - version_string: Versión legible (ej: "6.1.9.4")
            - build_string: Build como string
    """
    try:
        version = _sdk.NET_DVR_GetSDKVersion()
        build = _sdk.NET_DVR_GetSDKBuildVersion()
        return {
            "version": version,
            "build": build,
            "version_string": f"{version >> 24}.{(version >> 16) & 0xFF}.{(version >> 8) & 0xFF}.{version & 0xFF}",
            "build_string": f"{build}",
        }
    except Exception as e:
        return {"error": str(e)}


def get_last_error_info():
    """
    Obtiene información del último error del SDK

    Returns:
        dict: Información del error con keys:
            - code: Código de error (int)
            - message: Mensaje de error (str)
    """
    try:
        error_code = _sdk.NET_DVR_GetLastError()
        error_msg_ptr = _sdk.NET_DVR_GetErrorMsg(None)
        error_msg = (
            error_msg_ptr.decode("utf-8", errors="ignore")
            if error_msg_ptr
            else "Unknown error"
        )

        return {"code": error_code, "message": error_msg}
    except Exception as e:
        return {"error": str(e)}


def get_platform_info() -> dict:
    return {
        "platform": platform.system(),
        "sys_platform": sys.platform,
        "python": sys.version,
    }


__all__ = ["get_platform_info", "get_sdk_version", "get_last_error_info"]
