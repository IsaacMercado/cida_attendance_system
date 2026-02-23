from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_msc_screen_param import NET_DVR_MSC_SCREEN_PARAM


class struct_tagNET_DVR_MSC_SCREEN_PARAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_PARAM_CFG, [
    ('dwSize', DWORD),
    ('byParamType', BYTE),
    ('byRes1', BYTE * 3),
    ('struParam', NET_DVR_MSC_SCREEN_PARAM),
    ('byRes2', BYTE * 32),
])

NET_DVR_MSC_SCREEN_PARAM_CFG = struct_tagNET_DVR_MSC_SCREEN_PARAM_CFG
LPNET_DVR_MSC_SCREEN_PARAM_CFG = POINTER(struct_tagNET_DVR_MSC_SCREEN_PARAM_CFG)
tagNET_DVR_MSC_SCREEN_PARAM_CFG = struct_tagNET_DVR_MSC_SCREEN_PARAM_CFG
