from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_res_info import NET_DVR_RES_INFO


class struct_tagNET_DVR_VS_INPUT_CHAN_INIT(Structure):
    pass

_S(struct_tagNET_DVR_VS_INPUT_CHAN_INIT, [
    ('dwSize', DWORD),
    ('dwVSInputChan', DWORD),
    ('dwResNums', DWORD),
    ('struResList', NET_DVR_RES_INFO * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_VS_INPUT_CHAN_INIT = struct_tagNET_DVR_VS_INPUT_CHAN_INIT
LPNET_DVR_VS_INPUT_CHAN_INIT = POINTER(struct_tagNET_DVR_VS_INPUT_CHAN_INIT)
tagNET_DVR_VS_INPUT_CHAN_INIT = struct_tagNET_DVR_VS_INPUT_CHAN_INIT
