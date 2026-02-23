from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GUARD_COND(Structure):
    pass

_S(struct_tagNET_DVR_GUARD_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRelateType', BYTE),
    ('byGroupNo', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_GUARD_COND = struct_tagNET_DVR_GUARD_COND
LPNET_DVR_GUARD_COND = POINTER(struct_tagNET_DVR_GUARD_COND)
tagNET_DVR_GUARD_COND = struct_tagNET_DVR_GUARD_COND
