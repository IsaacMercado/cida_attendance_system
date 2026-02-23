from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MONITOR_LOCATION_COND(Structure):
    pass

_S(struct_tagNET_DVR_MONITOR_LOCATION_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRelateType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_MONITOR_LOCATION_COND = struct_tagNET_DVR_MONITOR_LOCATION_COND
LPNET_DVR_MONITOR_LOCATION_COND = POINTER(struct_tagNET_DVR_MONITOR_LOCATION_COND)
tagNET_DVR_MONITOR_LOCATION_COND = struct_tagNET_DVR_MONITOR_LOCATION_COND
