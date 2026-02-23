from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_system_time import NET_DVR_SYSTEM_TIME
from .net_its_traffic_drive_chan import NET_ITS_TRAFFIC_DRIVE_CHAN


class struct_tagNET_ITS_TRAFFIC_COLLECT(Structure):
    pass

_S(struct_tagNET_ITS_TRAFFIC_COLLECT, [
    ('dwSize', DWORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byLaneNum', BYTE),
    ('byDir', BYTE),
    ('byDetectType', BYTE),
    ('byRes1', BYTE),
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_SYSTEM_TIME),
    ('dwSamplePeriod', DWORD),
    ('struDriveChan', NET_ITS_TRAFFIC_DRIVE_CHAN * 6),
    ('byRes2', BYTE * 24),
])

NET_ITS_TRAFFIC_COLLECT = struct_tagNET_ITS_TRAFFIC_COLLECT
LPNET_ITS_TRAFFIC_COLLECT = POINTER(struct_tagNET_ITS_TRAFFIC_COLLECT)
tagNET_ITS_TRAFFIC_COLLECT = struct_tagNET_ITS_TRAFFIC_COLLECT
