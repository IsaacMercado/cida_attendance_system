from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVICE_RUN_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_RUN_STATUS, [
    ('dwSize', DWORD),
    ('dwMemoryTotal', DWORD),
    ('dwMemoryUsage', DWORD),
    ('byCPUUsage', BYTE),
    ('byMainFrameTemp', BYTE),
    ('byBackPanelTemp', BYTE),
    ('byRes1', BYTE * 1),
    ('byLeftDecResource', BYTE * 32),
    ('fNetworkFlow', c_float),
    ('byRes2', BYTE * 88),
])

NET_DVR_DEVICE_RUN_STATUS = struct_tagNET_DVR_DEVICE_RUN_STATUS
LPNET_DVR_DEVICE_RUN_STATUS = POINTER(struct_tagNET_DVR_DEVICE_RUN_STATUS)
tagNET_DVR_DEVICE_RUN_STATUS = struct_tagNET_DVR_DEVICE_RUN_STATUS
