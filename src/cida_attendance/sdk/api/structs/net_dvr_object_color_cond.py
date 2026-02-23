from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OBJECT_COLOR_COND(Structure):
    pass

_S(struct_tagNET_DVR_OBJECT_COLOR_COND, [
    ('dwChannel', DWORD),
    ('dwObjType', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_OBJECT_COLOR_COND = struct_tagNET_DVR_OBJECT_COLOR_COND
LPNET_DVR_OBJECT_COLOR_COND = POINTER(struct_tagNET_DVR_OBJECT_COLOR_COND)
tagNET_DVR_OBJECT_COLOR_COND = struct_tagNET_DVR_OBJECT_COLOR_COND
