from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_LOCKCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_LOCKCFG, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_PTZ_LOCKCFG = struct_tagNET_DVR_PTZ_LOCKCFG
LPNET_DVR_PTZ_LOCKCFG = POINTER(struct_tagNET_DVR_PTZ_LOCKCFG)
tagNET_DVR_PTZ_LOCKCFG = struct_tagNET_DVR_PTZ_LOCKCFG
