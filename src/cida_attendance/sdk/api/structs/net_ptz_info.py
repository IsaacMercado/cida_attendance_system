from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_PTZ_INFO(Structure):
    pass

_S(struct_tagNET_PTZ_INFO, [
    ('fPan', c_float),
    ('fTilt', c_float),
    ('fZoom', c_float),
    ('dwFocus', DWORD),
    ('byRes', BYTE * 4),
])

NET_PTZ_INFO = struct_tagNET_PTZ_INFO
LPNET_PTZ_INFO = POINTER(struct_tagNET_PTZ_INFO)
tagNET_PTZ_INFO = struct_tagNET_PTZ_INFO
