from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RTMP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RTMP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPacketLen', DWORD),
    ('szURL', c_char * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_RTMP_CFG = struct_tagNET_DVR_RTMP_CFG
LPNET_DVR_RTMP_CFG = POINTER(struct_tagNET_DVR_RTMP_CFG)
tagNET_DVR_RTMP_CFG = struct_tagNET_DVR_RTMP_CFG
