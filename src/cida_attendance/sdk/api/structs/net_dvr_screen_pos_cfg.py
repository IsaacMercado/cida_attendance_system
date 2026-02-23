from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_POS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_POS_CFG, [
    ('dwSize', DWORD),
    ('byScreenRowNum', BYTE),
    ('byScreenColNum', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_SCREEN_POS_CFG = struct_tagNET_DVR_SCREEN_POS_CFG
LPNET_DVR_SCREEN_POS_CFG = POINTER(struct_tagNET_DVR_SCREEN_POS_CFG)
tagNET_DVR_SCREEN_POS_CFG = struct_tagNET_DVR_SCREEN_POS_CFG
