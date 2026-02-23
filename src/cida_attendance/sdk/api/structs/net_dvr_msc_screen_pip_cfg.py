from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_MSC_SCREEN_PIP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_PIP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySubWindowSource', BYTE),
    ('bySubWindowBorderColor', BYTE),
    ('byRes1', BYTE),
    ('struPosition', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 16),
])

NET_DVR_MSC_SCREEN_PIP_CFG = struct_tagNET_DVR_MSC_SCREEN_PIP_CFG
LPNET_DVR_MSC_SCREEN_PIP_CFG = POINTER(struct_tagNET_DVR_MSC_SCREEN_PIP_CFG)
tagNET_DVR_MSC_SCREEN_PIP_CFG = struct_tagNET_DVR_MSC_SCREEN_PIP_CFG
