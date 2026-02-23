from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_VEHICLE_CONTROL_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_CONTROL_ALARM, [
    ('dwSize', DWORD),
    ('byListType', BYTE),
    ('byPlateType', BYTE),
    ('byPlateColor', BYTE),
    ('byRes1', BYTE),
    ('sLicense', c_char * 16),
    ('sCardNo', c_char * 48),
    ('struAlarmTime', NET_DVR_TIME_V30),
    ('dwChannel', DWORD),
    ('dwPicDataLen', DWORD),
    ('byPicType', BYTE),
    ('byPicTransType', BYTE),
    ('byRes3', BYTE * 2),
    ('pPicData', String),
    ('byRes2', BYTE * 48),
])

NET_DVR_VEHICLE_CONTROL_ALARM = struct_tagNET_DVR_VEHICLE_CONTROL_ALARM
LPNET_DVR_VEHICLE_CONTROL_ALARM = POINTER(struct_tagNET_DVR_VEHICLE_CONTROL_ALARM)
tagNET_DVR_VEHICLE_CONTROL_ALARM = struct_tagNET_DVR_VEHICLE_CONTROL_ALARM
