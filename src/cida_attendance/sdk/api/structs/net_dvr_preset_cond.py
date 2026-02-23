from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PRESET_COND(Structure):
    pass

_S(struct_tagNET_DVR_PRESET_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwGroupNO', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_PRESET_COND = struct_tagNET_DVR_PRESET_COND
LPNET_DVR_PRESET_COND = POINTER(struct_tagNET_DVR_PRESET_COND)
tagNET_DVR_PRESET_COND = struct_tagNET_DVR_PRESET_COND
