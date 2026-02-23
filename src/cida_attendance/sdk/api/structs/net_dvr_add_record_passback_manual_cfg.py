from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG, [
    ('dwSize', DWORD),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 128),
])

NET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG = struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG
LPNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG = POINTER(struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG)
tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG = struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_CFG
