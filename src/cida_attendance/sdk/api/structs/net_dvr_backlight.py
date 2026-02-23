from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKLIGHT(Structure):
    pass

_S(struct_tagNET_DVR_BACKLIGHT, [
    ('byBacklightMode', BYTE),
    ('byBacklightLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('dwPositionX1', DWORD),
    ('dwPositionY1', DWORD),
    ('dwPositionX2', DWORD),
    ('dwPositionY2', DWORD),
    ('byRes2', BYTE * 4),
])

NET_DVR_BACKLIGHT = struct_tagNET_DVR_BACKLIGHT
LPNET_DVR_BACKLIGHT = POINTER(struct_tagNET_DVR_BACKLIGHT)
tagNET_DVR_BACKLIGHT = struct_tagNET_DVR_BACKLIGHT
