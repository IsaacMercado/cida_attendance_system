from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_110 import NET_DVR_DISKSTATE
from .net_its_traffic_data_info import NET_ITS_TRAFFIC_DATA_INFO


class struct_tagNET_ITS_ECTWORKSTATE(Structure):
    pass

_S(struct_tagNET_ITS_ECTWORKSTATE, [
    ('dwSize', DWORD),
    ('byDevName', BYTE * 32),
    ('dwRunTime', DWORD),
    ('struTrafficDataInfo', NET_ITS_TRAFFIC_DATA_INFO * 2),
    ('dwMemoryUsage', DWORD),
    ('dwCpuUsage', DWORD),
    ('dwDevTemperature', DWORD),
    ('dwDeviceStatic', DWORD),
    ('struHardDiskStatic', NET_DVR_DISKSTATE * 33),
    ('byAlarmInStatic', BYTE * int((32 + 128))),
    ('byAlarmOutStatic', BYTE * int((32 + 64))),
    ('dwLocalDisplay', DWORD),
    ('byRes', BYTE * 256),
])

NET_ITS_ECTWORKSTATE = struct_tagNET_ITS_ECTWORKSTATE
LPNET_ITS_ECTWORKSTATE = POINTER(struct_tagNET_ITS_ECTWORKSTATE)
tagNET_ITS_ECTWORKSTATE = struct_tagNET_ITS_ECTWORKSTATE
