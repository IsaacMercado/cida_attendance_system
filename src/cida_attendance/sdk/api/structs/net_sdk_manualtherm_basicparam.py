from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_MANUALTHERM_BASICPARAM(Structure):
    pass

_S(struct_tagNET_SDK_MANUALTHERM_BASICPARAM, [
    ('dwSize', DWORD),
    ('wDistance', WORD),
    ('byDistanceUnit', BYTE),
    ('byRes1', BYTE * 1),
    ('fEmissivity', c_float),
    ('byRes', BYTE * 64),
])

NET_SDK_MANUALTHERM_BASICPARAM = struct_tagNET_SDK_MANUALTHERM_BASICPARAM
LPNET_SDK_MANUALTHERM_BASICPARAM = POINTER(struct_tagNET_SDK_MANUALTHERM_BASICPARAM)
tagNET_SDK_MANUALTHERM_BASICPARAM = struct_tagNET_SDK_MANUALTHERM_BASICPARAM
