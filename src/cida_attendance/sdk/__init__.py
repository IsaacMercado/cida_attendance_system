"""
SDK Completo de Hikvision

Este módulo contiene TODAS las funciones del SDK generadas automáticamente.

Uso:
    from cida_attendance.sdk import NET_DVR_Init, NET_DVR_Login_V40
    import cida_attendance.sdk as sdk  # Acceso directo a todos los símbolos

El archivo _generated.py contiene todas las funciones del SDK.
NO abras este archivo en el editor (es muy grande), solo impórtalo.

Para regenerar:
    uv run python scripts/generate_sdk/generate_sdk_bindings.py
"""

# Importar TODO desde el archivo generado
from cida_attendance.sdk._generated import *  # noqa: F403, F401

# Nota: no definimos __all__ para no incentivar `from ... import *`.
# El módulo sí expone los símbolos generados como atributos.
__all__ = []
