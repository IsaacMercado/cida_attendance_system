from ctypes import Structure, c_float

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_PTZ_INFO_EX(Structure):
    pass

_S(struct_tagNET_PTZ_INFO_EX, [
    ('fPan', c_float),
    ('fTilt', c_float),
    ('fVisibleZoom', c_float),
    ('dwVisibleFocus', DWORD),
    ('fThermalZoom', c_float),
    ('dwThermalFocus', DWORD),
])

NET_PTZ_INFO_EX = struct_tagNET_PTZ_INFO_EX
LPNET_PTZ_INFO_EX = POINTER(struct_tagNET_PTZ_INFO_EX)
tagNET_PTZ_INFO_EX = struct_tagNET_PTZ_INFO_EX
