from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPTICAL_DEHAZE(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_DEHAZE, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_OPTICAL_DEHAZE = struct_tagNET_DVR_OPTICAL_DEHAZE
LPNET_DVR_OPTICAL_DEHAZE = POINTER(struct_tagNET_DVR_OPTICAL_DEHAZE)
tagNET_DVR_OPTICAL_DEHAZE = struct_tagNET_DVR_OPTICAL_DEHAZE
