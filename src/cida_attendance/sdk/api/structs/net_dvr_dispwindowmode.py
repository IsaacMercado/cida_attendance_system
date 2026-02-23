from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPWINDOWMODE(Structure):
    pass

_S(struct_tagNET_DVR_DISPWINDOWMODE, [
    ('byDispChanType', BYTE),
    ('byDispChanSeq', BYTE),
    ('byRes', BYTE * 2),
    ('byDispMode', BYTE * 12),
])

NET_DVR_DISPWINDOWMODE = struct_tagNET_DVR_DISPWINDOWMODE
LPNET_DVR_DISPWINDOWMODE = POINTER(struct_tagNET_DVR_DISPWINDOWMODE)
tagNET_DVR_DISPWINDOWMODE = struct_tagNET_DVR_DISPWINDOWMODE
