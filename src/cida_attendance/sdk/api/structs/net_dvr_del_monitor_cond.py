from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEL_MONITOR_COND(Structure):
    pass

_S(struct_tagNET_DVR_DEL_MONITOR_COND, [
    ('dwSize', DWORD),
    ('byDelType', BYTE),
    ('dwAreaID', DWORD),
    ('dwMonitorID', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_DEL_MONITOR_COND = struct_tagNET_DVR_DEL_MONITOR_COND
LPNET_DVR_DEL_MONITOR_COND = POINTER(struct_tagNET_DVR_DEL_MONITOR_COND)
tagNET_DVR_DEL_MONITOR_COND = struct_tagNET_DVR_DEL_MONITOR_COND
