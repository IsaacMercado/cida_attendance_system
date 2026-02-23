from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VOICEBROADCAST_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VOICEBROADCAST_CFG, [
    ('dwSize', DWORD),
    ('sInfo', c_char * 128),
    ('byBroadcastNum', BYTE),
    ('byIntervalTime', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_VOICEBROADCAST_CFG = struct_tagNET_DVR_VOICEBROADCAST_CFG
LPNET_DVR_VOICEBROADCAST_CFG = POINTER(struct_tagNET_DVR_VOICEBROADCAST_CFG)
tagNET_DVR_VOICEBROADCAST_CFG = struct_tagNET_DVR_VOICEBROADCAST_CFG
