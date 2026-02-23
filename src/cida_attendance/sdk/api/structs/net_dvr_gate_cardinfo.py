from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_GATE_CARDINFO(Structure):
    pass

_S(struct_tagNET_DVR_GATE_CARDINFO, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('szCardNo', c_char * 48),
    ('szPassVehicleID', c_char * 32),
    ('szInVehicleID', c_char * 32),
    ('struSwipeTime', NET_DVR_TIME_V30),
    ('struCardTime', NET_DVR_TIME_V30),
    ('byLetPass', BYTE),
    ('byCardType', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_GATE_CARDINFO = struct_tagNET_DVR_GATE_CARDINFO
LPNET_DVR_GATE_CARDINFO = POINTER(struct_tagNET_DVR_GATE_CARDINFO)
tagNET_DVR_GATE_CARDINFO = struct_tagNET_DVR_GATE_CARDINFO
