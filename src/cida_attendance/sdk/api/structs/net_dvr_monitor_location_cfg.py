from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MONITOR_LOCATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MONITOR_LOCATION_CFG, [
    ('dwSize', DWORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byDirectionNo', BYTE),
    ('byRes1', BYTE * 3),
    ('byMonitorInfo', BYTE * 48),
    ('byRes', BYTE * 128),
])

NET_DVR_MONITOR_LOCATION_CFG = struct_tagNET_DVR_MONITOR_LOCATION_CFG
LPNET_DVR_MONITOR_LOCATION_CFG = POINTER(struct_tagNET_DVR_MONITOR_LOCATION_CFG)
tagNET_DVR_MONITOR_LOCATION_CFG = struct_tagNET_DVR_MONITOR_LOCATION_CFG
