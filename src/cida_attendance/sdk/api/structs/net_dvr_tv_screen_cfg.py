from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TV_SCREEN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TV_SCREEN_CFG, [
    ('dwSize', DWORD),
    ('dwPicStayTime', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_TV_SCREEN_CFG = struct_tagNET_DVR_TV_SCREEN_CFG
LPNET_DVR_TV_SCREEN_CFG = POINTER(struct_tagNET_DVR_TV_SCREEN_CFG)
tagNET_DVR_TV_SCREEN_CFG = struct_tagNET_DVR_TV_SCREEN_CFG
