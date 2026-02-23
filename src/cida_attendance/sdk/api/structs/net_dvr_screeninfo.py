from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREENINFO(Structure):
    pass

_S(struct_tagNET_DVR_SCREENINFO, [
    ('bySupportBigScreenNums', BYTE),
    ('byStartBigScreenNum', BYTE),
    ('byMaxScreenX', BYTE),
    ('byMaxScreenY', BYTE),
    ('byRes', BYTE * 8),
])

NET_DVR_SCREENINFO = struct_tagNET_DVR_SCREENINFO
LPNET_DVR_SCREENINFO = POINTER(struct_tagNET_DVR_SCREENINFO)
tagNET_DVR_SCREENINFO = struct_tagNET_DVR_SCREENINFO
