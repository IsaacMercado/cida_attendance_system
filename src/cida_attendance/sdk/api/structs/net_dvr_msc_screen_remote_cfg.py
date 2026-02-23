from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_msc_screen_param_cfg import NET_DVR_MSC_SCREEN_PARAM_CFG
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_MSC_SCREEN_REMOTE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_REMOTE_CFG, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('byRes1', BYTE * 3),
    ('struRectCfg', NET_DVR_RECTCFG_EX),
    ('struScreenParam', NET_DVR_MSC_SCREEN_PARAM_CFG),
    ('byRes2', BYTE * 32),
])

NET_DVR_MSC_SCREEN_REMOTE_CFG = struct_tagNET_DVR_MSC_SCREEN_REMOTE_CFG
LPNET_DVR_MSC_SCREEN_REMOTE_CFG = POINTER(struct_tagNET_DVR_MSC_SCREEN_REMOTE_CFG)
tagNET_DVR_MSC_SCREEN_REMOTE_CFG = struct_tagNET_DVR_MSC_SCREEN_REMOTE_CFG
