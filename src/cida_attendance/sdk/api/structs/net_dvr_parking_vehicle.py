from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_PARKING_VEHICLE(Structure):
    pass

_S(struct_tagNET_DVR_PARKING_VEHICLE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('szLicense', c_char * 16),
    ('szRelateCardNo', c_char * 48),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byVehicleType', BYTE),
    ('byPlateColor', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_PARKING_VEHICLE = struct_tagNET_DVR_PARKING_VEHICLE
LPNET_DVR_PARKING_VEHICLE = POINTER(struct_tagNET_DVR_PARKING_VEHICLE)
tagNET_DVR_PARKING_VEHICLE = struct_tagNET_DVR_PARKING_VEHICLE
