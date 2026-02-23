from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_dvr_tps_param import NET_DVR_TPS_PARAM


class struct_tagNET_DVR_TPS_REAL_TIME_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TPS_REAL_TIME_INFO, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('struTPSRealTimeInfo', NET_DVR_TPS_PARAM),
    ('pAddInfoBuffer', POINTER(BYTE)),
    ('byAddInfoFlag', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDeviceIDEx', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_TPS_REAL_TIME_INFO = struct_tagNET_DVR_TPS_REAL_TIME_INFO
LPNET_DVR_TPS_REAL_TIME_INFO = POINTER(struct_tagNET_DVR_TPS_REAL_TIME_INFO)
tagNET_DVR_TPS_REAL_TIME_INFO = struct_tagNET_DVR_TPS_REAL_TIME_INFO
