from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_108 import NET_DVR_CHANNELSTATE_V30
from .anon_110 import NET_DVR_DISKSTATE
from .net_its_traffic_data_info import NET_ITS_TRAFFIC_DATA_INFO


class struct_tagNET_ITS_WORKSTATE(Structure):
    pass

_S(struct_tagNET_ITS_WORKSTATE, [
    ('dwSize', DWORD),
    ('byDevName', BYTE * 32),
    ('dwRunTime', DWORD),
    ('struTrafficDataInfo', NET_ITS_TRAFFIC_DATA_INFO * 2),
    ('dwMemoryUsage', DWORD),
    ('dwCpuUsage', DWORD),
    ('dwDevTemperature', DWORD),
    ('dwDeviceStatic', DWORD),
    ('struHardDiskStatic', NET_DVR_DISKSTATE * 33),
    ('struChanStatic', NET_DVR_CHANNELSTATE_V30 * int((32 + 32))),
    ('byAlarmInStatic', BYTE * int((32 + 128))),
    ('byAlarmOutStatic', BYTE * int((32 + 64))),
    ('dwLocalDisplay', DWORD),
    ('byAudioInChanStatus', BYTE * 8),
    ('byRes', BYTE * 36),
])

NET_ITS_WORKSTATE = struct_tagNET_ITS_WORKSTATE
LPNET_ITS_WORKSTATE = POINTER(struct_tagNET_ITS_WORKSTATE)
tagNET_ITS_WORKSTATE = struct_tagNET_ITS_WORKSTATE
