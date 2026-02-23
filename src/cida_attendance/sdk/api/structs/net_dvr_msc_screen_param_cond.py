from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_MSC_SCREEN_PARAM_COND(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_PARAM_COND, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('byParamType', BYTE),
    ('byRes1', BYTE * 2),
    ('struRectCfg', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 32),
])

NET_DVR_MSC_SCREEN_PARAM_COND = struct_tagNET_DVR_MSC_SCREEN_PARAM_COND
LPNET_DVR_MSC_SCREEN_PARAM_COND = POINTER(struct_tagNET_DVR_MSC_SCREEN_PARAM_COND)
tagNET_DVR_MSC_SCREEN_PARAM_COND = struct_tagNET_DVR_MSC_SCREEN_PARAM_COND
