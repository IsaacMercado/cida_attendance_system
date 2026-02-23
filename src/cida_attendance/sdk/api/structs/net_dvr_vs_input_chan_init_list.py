from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vs_input_chan_init import NET_DVR_VS_INPUT_CHAN_INIT


class struct_tagNET_DVR_VS_INPUT_CHAN_INIT_LIST(Structure):
    pass

_S(struct_tagNET_DVR_VS_INPUT_CHAN_INIT_LIST, [
    ('dwSize', DWORD),
    ('struChanList', NET_DVR_VS_INPUT_CHAN_INIT * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_VS_INPUT_CHAN_INIT_LIST = struct_tagNET_DVR_VS_INPUT_CHAN_INIT_LIST
LPNET_DVR_VS_INPUT_CHAN_INIT_LIST = POINTER(struct_tagNET_DVR_VS_INPUT_CHAN_INIT_LIST)
tagNET_DVR_VS_INPUT_CHAN_INIT_LIST = struct_tagNET_DVR_VS_INPUT_CHAN_INIT_LIST
