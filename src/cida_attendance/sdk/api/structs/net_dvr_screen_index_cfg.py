from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_base_info import NET_DVR_SCREEN_BASE_INFO


class struct_tagNET_DVR_SCREEN_INDEX_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_INDEX_CFG, [
    ('dwSize', DWORD),
    ('byEnbale', BYTE),
    ('byDevAddType', BYTE),
    ('byRes1', BYTE * 2),
    ('struScreenBaseInfo', NET_DVR_SCREEN_BASE_INFO),
    ('byRes', BYTE * 32),
])

NET_DVR_SCREEN_INDEX_CFG = struct_tagNET_DVR_SCREEN_INDEX_CFG
LPNET_DVR_SCREEN_INDEX_CFG = POINTER(struct_tagNET_DVR_SCREEN_INDEX_CFG)
tagNET_DVR_SCREEN_INDEX_CFG = struct_tagNET_DVR_SCREEN_INDEX_CFG
