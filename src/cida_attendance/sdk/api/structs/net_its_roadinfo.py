from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_its_single_device_info import NET_ITS_SINGLE_DEVICE_INFO


class struct_tagNET_ITS_ROADINFO(Structure):
    pass

_S(struct_tagNET_ITS_ROADINFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byTriggerMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDeviceNum', DWORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byRoadInfo', BYTE * 48),
    ('struSingleDevice', NET_ITS_SINGLE_DEVICE_INFO * 32),
    ('byRes', BYTE * 16),
])

NET_ITS_ROADINFO = struct_tagNET_ITS_ROADINFO
LPNET_ITS_ROADINFO = POINTER(struct_tagNET_ITS_ROADINFO)
tagNET_ITS_ROADINFO = struct_tagNET_ITS_ROADINFO
