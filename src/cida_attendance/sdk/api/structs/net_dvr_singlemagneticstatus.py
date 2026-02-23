from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SingleMagneticStatus_(Structure):
    pass

_S(struct_tagNET_DVR_SingleMagneticStatus_, [
    ('dwSize', DWORD),
    ('sDetectorID', c_char * 16),
    ('sManagerID', c_char * 16),
    ('sParkNum', c_char * 16),
    ('struDetectorTime', NET_DVR_TIME_V30),
    ('dwRssi', DWORD),
    ('byParkinglotState', BYTE),
    ('byBatteryState', BYTE),
    ('byDeviceState', BYTE),
    ('byCMD', BYTE),
    ('byRes', BYTE * 184),
])

NET_DVR_SingleMagneticStatus = struct_tagNET_DVR_SingleMagneticStatus_
LPNET_DVR_SingleMagneticStatus = POINTER(struct_tagNET_DVR_SingleMagneticStatus_)
tagNET_DVR_SingleMagneticStatus_ = struct_tagNET_DVR_SingleMagneticStatus_
