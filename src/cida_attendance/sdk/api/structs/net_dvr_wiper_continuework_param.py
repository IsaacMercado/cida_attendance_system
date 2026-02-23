from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIPER_CONTINUEWORK_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_WIPER_CONTINUEWORK_PARAM, [
    ('byWorkTimeInterval', BYTE),
    ('byRes', BYTE * 3),
    ('dwContinueWorkTime', DWORD),
    ('byRes1', BYTE * 8),
])

NET_DVR_WIPER_CONTINUEWORK_PARAM = struct_tagNET_DVR_WIPER_CONTINUEWORK_PARAM
LPNET_DVR_WIPER_CONTINUEWORK_PARAM = POINTER(struct_tagNET_DVR_WIPER_CONTINUEWORK_PARAM)
tagNET_DVR_WIPER_CONTINUEWORK_PARAM = struct_tagNET_DVR_WIPER_CONTINUEWORK_PARAM
