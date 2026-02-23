from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RESET_COUNTER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RESET_COUNTER_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byMode', BYTE),
    ('byRes1', BYTE * 2),
    ('struTime', NET_DVR_TIME_EX * 7),
    ('byRes', BYTE * 64),
])

NET_DVR_RESET_COUNTER_CFG = struct_tagNET_DVR_RESET_COUNTER_CFG
LPNET_DVR_RESET_COUNTER_CFG = POINTER(struct_tagNET_DVR_RESET_COUNTER_CFG)
tagNET_DVR_RESET_COUNTER_CFG = struct_tagNET_DVR_RESET_COUNTER_CFG
