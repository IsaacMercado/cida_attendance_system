from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_SIGNAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_SIGNAL_CFG, [
    ('dwSize', DWORD),
    ('bySignalSourceType', BYTE),
    ('byNoSignalPic', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_SCREEN_SIGNAL_CFG = struct_tagNET_DVR_SCREEN_SIGNAL_CFG
LPNET_DVR_SCREEN_SIGNAL_CFG = POINTER(struct_tagNET_DVR_SCREEN_SIGNAL_CFG)
tagNET_DVR_SCREEN_SIGNAL_CFG = struct_tagNET_DVR_SCREEN_SIGNAL_CFG
