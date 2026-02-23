from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_chan_info import NET_DVR_PU_CHAN_INFO


class struct_tagNET_DVR_PU_CHAN_LIST(Structure):
    pass

_S(struct_tagNET_DVR_PU_CHAN_LIST, [
    ('dwSize', DWORD),
    ('dwNum', DWORD),
    ('struPuChanInfo', NET_DVR_PU_CHAN_INFO * 512),
])

NET_DVR_PU_CHAN_LIST = struct_tagNET_DVR_PU_CHAN_LIST
LPNET_DVR_PU_CHAN_LIST = POINTER(struct_tagNET_DVR_PU_CHAN_LIST)
tagNET_DVR_PU_CHAN_LIST = struct_tagNET_DVR_PU_CHAN_LIST
