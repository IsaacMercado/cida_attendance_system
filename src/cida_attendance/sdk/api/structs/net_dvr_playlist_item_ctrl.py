from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_play_item import NET_DVR_PLAY_ITEM


class struct_tagNET_DVR_PLAYLIST_ITEM_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_PLAYLIST_ITEM_CTRL, [
    ('dwSize', DWORD),
    ('byCtrlType', BYTE),
    ('byPlayIndex', BYTE),
    ('struPlayItem', NET_DVR_PLAY_ITEM),
    ('byNewPlayIndex', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_PLAYLIST_ITEM_CTRL = struct_tagNET_DVR_PLAYLIST_ITEM_CTRL
LPNET_DVR_PLAYLIST_ITEM_CTRL = POINTER(struct_tagNET_DVR_PLAYLIST_ITEM_CTRL)
tagNET_DVR_PLAYLIST_ITEM_CTRL = struct_tagNET_DVR_PLAYLIST_ITEM_CTRL
