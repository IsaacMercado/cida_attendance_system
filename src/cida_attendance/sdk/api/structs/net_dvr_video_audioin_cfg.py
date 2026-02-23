from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_AUDIOIN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_AUDIOIN_CFG, [
    ('dwSize', DWORD),
    ('dwChanNo', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_VIDEO_AUDIOIN_CFG = struct_tagNET_DVR_VIDEO_AUDIOIN_CFG
LPNET_DVR_VIDEO_AUDIOIN_CFG = POINTER(struct_tagNET_DVR_VIDEO_AUDIOIN_CFG)
tagNET_DVR_VIDEO_AUDIOIN_CFG = struct_tagNET_DVR_VIDEO_AUDIOIN_CFG
