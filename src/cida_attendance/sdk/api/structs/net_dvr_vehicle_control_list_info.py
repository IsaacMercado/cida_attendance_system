from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_VEHICLE_CONTROL_LIST_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_CONTROL_LIST_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwDataIndex', DWORD),
    ('sLicense', c_char * 16),
    ('byListType', BYTE),
    ('byPlateType', BYTE),
    ('byPlateColor', BYTE),
    ('byRes', BYTE * 21),
    ('sCardNo', c_char * 48),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struStopTime', NET_DVR_TIME_V30),
    ('sOperateIndex', c_char * 32),
    ('byRes1', BYTE * 224),
])

NET_DVR_VEHICLE_CONTROL_LIST_INFO = struct_tagNET_DVR_VEHICLE_CONTROL_LIST_INFO
LPNET_DVR_VEHICLE_CONTROL_LIST_INFO = POINTER(struct_tagNET_DVR_VEHICLE_CONTROL_LIST_INFO)
tagNET_DVR_VEHICLE_CONTROL_LIST_INFO = struct_tagNET_DVR_VEHICLE_CONTROL_LIST_INFO
