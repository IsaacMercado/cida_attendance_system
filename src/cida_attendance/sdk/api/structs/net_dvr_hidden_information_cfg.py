from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pos_hidden_information import NET_DVR_POS_HIDDEN_INFORMATION


class struct_tagNET_DVR_HIDDEN_INFORMATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HIDDEN_INFORMATION_CFG, [
    ('dwSize', DWORD),
    ('byFuncType', BYTE),
    ('Res1', BYTE * 3),
    ('struPosInfo', NET_DVR_POS_HIDDEN_INFORMATION),
    ('byRes', BYTE * 1024),
])

NET_DVR_HIDDEN_INFORMATION_CFG = struct_tagNET_DVR_HIDDEN_INFORMATION_CFG
LPNET_DVR_HIDDEN_INFORMATION_CFG = POINTER(struct_tagNET_DVR_HIDDEN_INFORMATION_CFG)
tagNET_DVR_HIDDEN_INFORMATION_CFG = struct_tagNET_DVR_HIDDEN_INFORMATION_CFG
