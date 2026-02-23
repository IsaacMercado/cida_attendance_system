from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BIG_SCREEN_AUDIO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BIG_SCREEN_AUDIO_CFG, [
    ('dwSize', DWORD),
    ('dwWinIndex', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_BIG_SCREEN_AUDIO_CFG = struct_tagNET_DVR_BIG_SCREEN_AUDIO_CFG
LPNET_DVR_BIG_SCREEN_AUDIO_CFG = POINTER(struct_tagNET_DVR_BIG_SCREEN_AUDIO_CFG)
tagNET_DVR_BIG_SCREEN_AUDIO_CFG = struct_tagNET_DVR_BIG_SCREEN_AUDIO_CFG
