from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_VEHICLE_CHECK(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_CHECK, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('wIllegalType', WORD),
    ('byRes', BYTE * 2),
    ('sIllegalTypeInfo', c_char * 128),
    ('struIllegalTime', NET_DVR_TIME_V30),
    ('byIllegalVehicleNum', BYTE),
    ('byRes1', BYTE * 3),
    ('sCustomInfo', c_char * 64),
    ('byRes2', BYTE * 128),
])

NET_DVR_VEHICLE_CHECK = struct_tagNET_DVR_VEHICLE_CHECK
LPNET_DVR_VEHICLE_CHECK = POINTER(struct_tagNET_DVR_VEHICLE_CHECK)
tagNET_DVR_VEHICLE_CHECK = struct_tagNET_DVR_VEHICLE_CHECK
