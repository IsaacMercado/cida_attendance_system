import ctypes
import datetime
from typing import Any, Callable

from cida_attendance import sdk
from cida_attendance.sdk.bindings import build_datetime_from_net_dvr_time

# Conditional field rules for structures
# Format: {
#   "StructureName": {
#       "target_field": ("flag_field", expected_value),
#       # or include + cast to concrete ctypes struct:
#       "target_field": ("flag_field", expected_value, sdk.NET_DVR_SOME_STRUCT),
#   }
# }
ConditionalFieldsType = dict[
    str,
    dict[
        str,
        tuple[str, Any]
        | tuple[str, Any, type[ctypes.Structure] | type[ctypes.Union]]
        | Callable,
    ],
]
CONDITIONAL_FIELDS: ConditionalFieldsType = {
    "NET_DVR_ACS_ALARM_INFO": {
        "pAcsEventInfoExtend": (
            "byAcsEventInfoExtend",
            1,
            sdk.NET_DVR_ACS_EVENT_INFO_EXTEND,
        ),
        "pAcsEventInfoExtendV20": (
            "byAcsEventInfoExtendV20",
            1,
            sdk.NET_DVR_ACS_EVENT_INFO_EXTEND_V20,
        ),
    },
}


def _normalize_struct_name(name: str) -> str:
    if name.startswith("struct_tag"):
        return name[len("struct_tag") :]
    if name.startswith("union_tag"):
        return name[len("union_tag") :]
    return name


def _extract_address(value: Any) -> int | None:
    if value is None:
        return None

    # c_void_p
    if isinstance(value, ctypes.c_void_p):
        return int(value.value) if value.value else None

    # c_char_p
    if isinstance(value, ctypes.c_char_p):
        try:
            addr = ctypes.cast(value, ctypes.c_void_p).value
            return int(addr) if addr else None
        except Exception:
            return None

    # SDK generated String union (char*)
    try:
        sdk_string_type = getattr(sdk, "String", None)
        if sdk_string_type is not None and isinstance(value, sdk_string_type):
            raw_ptr = getattr(value, "raw", None)
            if raw_ptr is None:
                return None
            try:
                addr = ctypes.cast(raw_ptr, ctypes.c_void_p).value
                return int(addr) if addr else None
            except Exception:
                return None
    except Exception:
        pass

    # Generic pointer-like values
    try:
        addr = ctypes.cast(value, ctypes.c_void_p).value
        return int(addr) if addr else None
    except Exception:
        return None


def _cast_pointer_to_ctype(
    value: Any,
    target_ctype: type[ctypes.Structure] | type[ctypes.Union],
) -> Any:
    addr = _extract_address(value)
    if not addr:
        return None

    try:
        ptr = ctypes.cast(ctypes.c_void_p(addr), ctypes.POINTER(target_ctype))
        return ptr.contents
    except Exception:
        return int(addr)


def ctypes_to_dict(
    value: Any,
    *,
    tz: datetime.tzinfo | None = None,
    encoding: str = "ascii",
    errors: str = "replace",
    max_depth: int = 8,
    conditional_fields: ConditionalFieldsType | None = None,
    bytes_as_str: bool = True,
    _depth: int = 0,
) -> Any:
    """Convert `ctypes` values to Python types.

    Useful for serializing SDK structures without manually mapping fields.

    Handles:
    - `ctypes.Structure` / `ctypes.Union` -> dict
    - arrays -> list or str (if `c_char[]`) or bytes (if `BYTE[]`)
    - pointers -> `None` if NULL, or the content (if pointing to struct/primitive)
    - `c_char_p` -> str/None
    - `c_void_p` -> int/None
    - ctypes primitives -> int/float/bool

    Args:
        conditional_fields: Rules for including fields conditionally.
            Format: {
                "StructureName": {
                    "field": ("flag_field", expected_value),
                    # or ("flag_field", expected_value, target_ctype)
                    # or
                    "field": lambda struct: bool_expr,
                }
            }
            If not specified, uses global CONDITIONAL_FIELDS.
    """

    if conditional_fields is None:
        conditional_fields = CONDITIONAL_FIELDS

    if _depth >= max_depth:
        return "<max_depth>"

    if value is None:
        return None

    # Special case: NET_DVR_TIME (dwYear..dwSecond) -> datetime
    # Note: in the generated wrapper, `sdk.NET_DVR_TIME` is an alias to a ctypes class.
    try:
        if isinstance(value, sdk.NET_DVR_TIME):
            return build_datetime_from_net_dvr_time(value, tz=tz)  # type: ignore[arg-type]
    except Exception:
        pass

    # Void pointer
    if isinstance(value, ctypes.c_void_p):
        return int(value.value) if value.value else None

    # c_char_p (string)
    if isinstance(value, ctypes.c_char_p):
        if not value.value:
            return None
        return value.value.decode(encoding, errors=errors)

    # SDK generated String union (char*)
    try:
        sdk_string_type = getattr(sdk, "String", None)
        if sdk_string_type is not None and isinstance(value, sdk_string_type):
            addr = _extract_address(value)
            return int(addr) if addr else None
    except Exception:
        pass

    # Structures / Unions
    if isinstance(value, (ctypes.Structure, ctypes.Union)):
        out: dict[str, Any] = {}

        # Get conditional rules for this structure
        struct_name = type(value).__name__
        struct_alias = _normalize_struct_name(struct_name)
        struct_rules = conditional_fields.get(struct_alias) or conditional_fields.get(
            struct_name,
            {},
        )

        for field_name, _field_type in getattr(value, "_fields_", []):
            # Check if this field has a condition
            if field_name in struct_rules:
                rule = struct_rules[field_name]
                cast_target: type[ctypes.Structure] | type[ctypes.Union] | None = None

                # If it's a tuple (flag_field, expected_value)
                if isinstance(rule, tuple):
                    if len(rule) == 2:
                        flag_field, expected_value = rule
                    elif len(rule) == 3:
                        flag_field, expected_value, cast_target = rule
                    else:
                        # Invalid rule shape; skip conversion for safety
                        continue

                    try:
                        flag_value = getattr(value, flag_field)
                        # Convert to Python value if it's ctypes
                        if isinstance(flag_value, ctypes._SimpleCData):  # type: ignore[attr-defined]
                            flag_value = flag_value.value

                        # If it doesn't match, skip this field
                        if flag_value != expected_value:
                            continue
                    except AttributeError:
                        # Flag field doesn't exist, skip
                        continue

                # If it's a callable (lambda/function)
                elif callable(rule):
                    try:
                        if not rule(value):
                            continue
                    except Exception:
                        # If evaluation fails, skip the field
                        continue

            try:
                field_val = getattr(value, field_name)
            except Exception:
                continue

            # Optional conditional cast (typically char* -> specific SDK struct)
            if field_name in struct_rules:
                rule = struct_rules[field_name]
                if isinstance(rule, tuple) and len(rule) == 3:
                    target_ctype = rule[2]
                    field_val = _cast_pointer_to_ctype(field_val, target_ctype)

            out[field_name] = ctypes_to_dict(
                field_val,
                tz=tz,
                encoding=encoding,
                errors=errors,
                max_depth=max_depth,
                conditional_fields=conditional_fields,
                bytes_as_str=bytes_as_str,
                _depth=_depth + 1,
            )
        return out

    # Arrays
    if isinstance(value, ctypes.Array):
        element_type = getattr(value, "_type_", None)
        if element_type is ctypes.c_char:
            raw = bytes(value)
            return bytes_to_str(raw, encoding=encoding, errors=errors)

        # Byte array (c_ubyte/c_byte) usually represents binary buffer
        if element_type in (ctypes.c_ubyte, ctypes.c_byte):
            # Return raw bytes to be more general.
            # (We don't try to guess if it's text; the caller decides.)
            try:
                raw = ctypes.string_at(ctypes.addressof(value), ctypes.sizeof(value))
            except Exception:
                # Conservative fallback.
                raw = bytes(int(b) & 0xFF for b in value)

            if bytes_as_str:
                return bytes_to_str(raw, encoding=encoding, errors=errors)
            return raw

        return [
            ctypes_to_dict(
                value[i],
                tz=tz,
                encoding=encoding,
                errors=errors,
                max_depth=max_depth,
                conditional_fields=conditional_fields,
                bytes_as_str=bytes_as_str,
                _depth=_depth + 1,
            )
            for i in range(len(value))
        ]

    # Pointers (LP_*)
    pointer_base = getattr(ctypes, "_Pointer", None)
    if pointer_base is not None and isinstance(value, pointer_base):
        # Important: DO NOT use `hasattr(value, "contents")`.
        # In ctypes, `.contents` can raise `ValueError: NULL pointer access`
        # and `hasattr()` propagates exceptions other than AttributeError.

        try:
            addr = ctypes.cast(value, ctypes.c_void_p).value
        except Exception:
            addr = None

        if not addr:
            return None

        pointee_type = getattr(value, "_type_", None)
        # Pointer to char => without length it's not safe to dereference; return addr.
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
                conditional_fields=conditional_fields,
                bytes_as_str=bytes_as_str,
                _depth=_depth + 1,
            )
        except Exception:
            return int(addr)

    # ctypes primitives
    if isinstance(value, ctypes._SimpleCData):  # type: ignore[attr-defined]
        # BOOL/byte/word/dword/etc.
        return value.value

    # Native bytes
    if isinstance(value, (bytes, bytearray)):
        return bytes(value)

    return value


def bytes_to_str(b: bytes, encoding: str = "ascii", errors: str = "replace") -> str:
    return b.decode(encoding, errors=errors).rstrip("\x00")
