from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALL_WIN_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_WALL_WIN_STATUS, [
    ('dwSize', DWORD),
    ('byDecodeStatus', BYTE),
    ('byStreamType', BYTE),
    ('byPacketType', BYTE),
    ('byFpsDecV', BYTE),
    ('byFpsDecA', BYTE),
    ('byRes1', BYTE * 7),
    ('dwDecodedV', DWORD),
    ('dwDecodedA', DWORD),
    ('wImgW', WORD),
    ('wImgH', WORD),
    ('byStreamMode', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_WALL_WIN_STATUS = struct_tagNET_DVR_WALL_WIN_STATUS
LPNET_DVR_WALL_WIN_STATUS = POINTER(struct_tagNET_DVR_WALL_WIN_STATUS)
tagNET_DVR_WALL_WIN_STATUS = struct_tagNET_DVR_WALL_WIN_STATUS
