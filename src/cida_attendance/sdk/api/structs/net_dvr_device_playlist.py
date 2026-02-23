from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_play_item import NET_DVR_PLAY_ITEM


class struct_tagNET_DVR_DEVICE_PLAYLIST(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_PLAYLIST, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byPlayType', BYTE),
    ('byVaildItemNum', BYTE),
    ('byRes', BYTE * 1),
    ('struPlayItem', NET_DVR_PLAY_ITEM * 64),
    ('byPlaylistName', BYTE * 64),
    ('dwPlaylistNo', DWORD),
    ('byRes2', BYTE * 128),
])

NET_DVR_DEVICE_PLAYLIST = struct_tagNET_DVR_DEVICE_PLAYLIST
LPNET_DVR_DEVICE_PLAYLIST = POINTER(struct_tagNET_DVR_DEVICE_PLAYLIST)
tagNET_DVR_DEVICE_PLAYLIST = struct_tagNET_DVR_DEVICE_PLAYLIST
