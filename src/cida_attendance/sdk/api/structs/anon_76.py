from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_anon_76(Structure):
    pass

_S(struct_anon_76, [
    ('dwSize', DWORD),
    ('dwIndex', DWORD),
    ('byDeviceID', BYTE * 48),
    ('byBelieve', BYTE),
    ('byDir', BYTE),
    ('byLineID', BYTE),
    ('byRes1', BYTE),
    ('struSnapTime', NET_DVR_TIME_EX),
    ('sLicense', c_char * 32),
    ('byMonitoringSiteID', BYTE * 48),
    ('byCountry', BYTE),
    ('byMatchingResult', BYTE),
    ('byArea', BYTE),
    ('byPlateType', BYTE),
    ('sDeviceName', c_char * 32),
    ('byPlateColor', BYTE),
    ('byPlateSize', BYTE),
    ('byRes2', BYTE * 2),
    ('sPlateCategory', c_char * 8),
    ('sPlateImageURL', c_char * 256),
    ('sEffectiveTime', c_char * 32),
    ('byRes', BYTE * 176),
])

NET_DVR_VEHICLE_INFO_CFG = struct_anon_76
LPNET_DVR_VEHICLE_INFO_CFG = POINTER(struct_anon_76)
