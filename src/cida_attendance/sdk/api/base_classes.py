from ctypes import (
    Structure,
    c_int,
    c_longlong,
    c_short,
    c_ubyte,
    c_uint,
    c_ulonglong,
    c_ushort,
)
from typing import Any

from .ctypes_preamble import POINTER


def _S(cls: Structure, fields: list[tuple[str, Any]], pack=None, anon=None):
    if pack:
        cls._pack_ = pack
    if anon:
        cls._anonymous_ = anon
    cls._fields_ = fields
    cls.__slots__ = [n for n, *_ in fields]

DWORD = c_uint
WORD = c_ushort
USHORT = c_ushort
SHORT = c_short
LONG = c_int
BYTE = c_ubyte
UINT = c_uint
LPVOID = POINTER(None)
HANDLE = POINTER(None)
LPDWORD = POINTER(c_uint)
UINT64 = c_ulonglong
INT64 = c_longlong
COLORKEY = c_uint
COLORREF = c_uint
HWND = c_uint
BOOL = c_int
