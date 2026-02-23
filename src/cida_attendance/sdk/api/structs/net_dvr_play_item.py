from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLAY_ITEM(Structure):
    pass

_S(struct_tagNET_DVR_PLAY_ITEM, [
    ('dwSize', DWORD),
    ('byItemType', BYTE),
    ('byRes', BYTE * 3),
    ('dwPlayManageNo', DWORD),
    ('dwPlayPicTime', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_PLAY_ITEM = struct_tagNET_DVR_PLAY_ITEM
LPNET_DVR_PLAY_ITEM = POINTER(struct_tagNET_DVR_PLAY_ITEM)
tagNET_DVR_PLAY_ITEM = struct_tagNET_DVR_PLAY_ITEM
