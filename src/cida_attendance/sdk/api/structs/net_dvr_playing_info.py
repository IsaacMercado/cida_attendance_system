from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_playitem_info import NET_DVR_PLAYITEM_INFO


class struct_tagNET_DVR_PLAYING_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PLAYING_INFO, [
    ('dwSize', DWORD),
    ('byPlayWay', BYTE),
    ('byCurPlayType', BYTE),
    ('byPlayState', BYTE),
    ('byAudioState', BYTE),
    ('struPlayItemInfo', NET_DVR_PLAYITEM_INFO),
    ('byRes2', BYTE * 16),
])

NET_DVR_PLAYING_INFO = struct_tagNET_DVR_PLAYING_INFO
LPNET_DVR_PLAYING_INFO = POINTER(struct_tagNET_DVR_PLAYING_INFO)
tagNET_DVR_PLAYING_INFO = struct_tagNET_DVR_PLAYING_INFO
