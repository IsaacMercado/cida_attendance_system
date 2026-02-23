from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_COND(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('wPresetNo', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_THERMOMETRY_COND = struct_tagNET_DVR_THERMOMETRY_COND
LPNET_DVR_THERMOMETRY_COND = POINTER(struct_tagNET_DVR_THERMOMETRY_COND)
tagNET_DVR_THERMOMETRY_COND = struct_tagNET_DVR_THERMOMETRY_COND
