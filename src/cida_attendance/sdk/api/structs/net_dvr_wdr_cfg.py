from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_wdr import NET_DVR_WDR


class struct_tagNET_DVR_WDR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WDR_CFG, [
    ('dwSize', DWORD),
    ('struWDR', NET_DVR_WDR),
])

NET_DVR_WDR_CFG = struct_tagNET_DVR_WDR_CFG
LPNET_DVR_WDR_CFG = POINTER(struct_tagNET_DVR_WDR_CFG)
tagNET_DVR_WDR_CFG = struct_tagNET_DVR_WDR_CFG
