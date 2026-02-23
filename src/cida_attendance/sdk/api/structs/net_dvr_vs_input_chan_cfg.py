from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_res_info import NET_DVR_RES_INFO


class struct_tagNET_DVR_VS_INPUT_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VS_INPUT_CHAN_CFG, [
    ('dwSize', DWORD),
    ('dwVSInputChan', DWORD),
    ('struResolutin', NET_DVR_RES_INFO),
    ('byRes', BYTE * 64),
])

NET_DVR_VS_INPUT_CHAN_CFG = struct_tagNET_DVR_VS_INPUT_CHAN_CFG
LPNET_DVR_VS_INPUT_CHAN_CFG = POINTER(struct_tagNET_DVR_VS_INPUT_CHAN_CFG)
tagNET_DVR_VS_INPUT_CHAN_CFG = struct_tagNET_DVR_VS_INPUT_CHAN_CFG
