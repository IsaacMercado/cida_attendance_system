import ctypes
import datetime
from typing import Any

from cida_attendance import sdk
from cida_attendance.sdk.bindings import build_datetime_from_net_dvr_time


def ctypes_to_dict(
    value: Any,
    *,
    tz: datetime.tzinfo | None = None,
    encoding: str = "ascii",
    errors: str = "replace",
    max_depth: int = 8,
    _depth: int = 0,
    _field_name: str | None = None,
) -> Any:
    """Convierte valores `ctypes` a tipos Python.

    Útil para serializar estructuras del SDK sin mapear campos a mano.

    Maneja:
    - `ctypes.Structure` / `ctypes.Union` -> dict
    - arrays -> list o str (si es `c_char[]`) o bytes (si es `BYTE[]`)
    - punteros -> `None` si NULL, o el contenido (si apunta a struct/primitivo)
    - `c_char_p` -> str/None
    - `c_void_p` -> int/None
    - primitivos ctypes -> int/float/bool
    """

    if _depth >= max_depth:
        return "<max_depth>"

    if value is None:
        return None

    # Caso especial: NET_DVR_TIME (dwYear..dwSecond) -> datetime
    # Nota: en el wrapper generado, `sdk.NET_DVR_TIME` es un alias a una clase ctypes.
    try:
        if isinstance(value, sdk.NET_DVR_TIME):
            return build_datetime_from_net_dvr_time(value, tz=tz)  # type: ignore[arg-type]
    except Exception:
        pass

    # Puntero void
    if isinstance(value, ctypes.c_void_p):
        return int(value.value) if value.value else None

    # c_char_p (string)
    if isinstance(value, ctypes.c_char_p):
        if not value.value:
            return None
        return value.value.decode(encoding, errors=errors)

    # Estructuras / Unions
    if isinstance(value, (ctypes.Structure, ctypes.Union)):
        out: dict[str, Any] = {}
        for field_name, _field_type in getattr(value, "_fields_", []):
            try:
                field_val = getattr(value, field_name)
            except Exception:
                continue
            out[field_name] = ctypes_to_dict(
                field_val,
                tz=tz,
                encoding=encoding,
                errors=errors,
                max_depth=max_depth,
                _depth=_depth + 1,
                _field_name=field_name,
            )
        return out

    # Arrays
    if isinstance(value, ctypes.Array):
        element_type = getattr(value, "_type_", None)
        if element_type is ctypes.c_char:
            raw = bytes(value)
            raw = raw.split(b"\x00", 1)[0]
            return raw.decode(encoding, errors=errors)

        # Array de bytes (c_ubyte/c_byte) normalmente representa buffer binario
        if element_type in (ctypes.c_ubyte, ctypes.c_byte):
            # Devuelve bytes crudos para ser más general.
            # (No intentamos adivinar si es texto; el caller decide.)
            try:
                return ctypes.string_at(ctypes.addressof(value), ctypes.sizeof(value))
            except Exception:
                # Fallback conservador.
                return bytes(int(b) & 0xFF for b in value)

        return [
            ctypes_to_dict(
                value[i],
                tz=tz,
                encoding=encoding,
                errors=errors,
                max_depth=max_depth,
                _depth=_depth + 1,
            )
            for i in range(len(value))
        ]

    # Punteros (LP_*)
    pointer_base = getattr(ctypes, "_Pointer", None)
    if pointer_base is not None and isinstance(value, pointer_base):
        # Importante: NO usar `hasattr(value, "contents")`.
        # En ctypes, `.contents` puede lanzar `ValueError: NULL pointer access`
        # y `hasattr()` propaga excepciones que no sean AttributeError.

        try:
            addr = ctypes.cast(value, ctypes.c_void_p).value
        except Exception:
            addr = None

        if not addr:
            return None

        pointee_type = getattr(value, "_type_", None)
        # Puntero a char => sin longitud no es seguro dereferenciar; devolvemos addr.
        if pointee_type is ctypes.c_char:
            return int(addr)

        try:
            pointee = value.contents
        except ValueError:
            return None
        except Exception:
            return int(addr)

        try:
            return ctypes_to_dict(
                pointee,
                tz=tz,
                encoding=encoding,
                errors=errors,
                max_depth=max_depth,
                _depth=_depth + 1,
            )
        except Exception:
            return int(addr)

    # Primitivos ctypes
    if isinstance(value, ctypes._SimpleCData):  # type: ignore[attr-defined]
        # BOOL/byte/word/dword/etc.
        return value.value

    # Bytes nativos
    if isinstance(value, (bytes, bytearray)):
        return bytes(value)

    return value
