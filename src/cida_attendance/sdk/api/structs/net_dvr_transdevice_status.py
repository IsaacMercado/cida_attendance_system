from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRANSDEVICE_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_TRANSDEVICE_STATUS, [
    ('dwSize', DWORD),
    ('dwTotalResource', DWORD),
    ('dwIdleResource', DWORD),
    ('byCpuLoad', BYTE),
    ('byRes', BYTE * 67),
])

NET_DVR_TRANSDEVICE_STATUS = struct_tagNET_DVR_TRANSDEVICE_STATUS
LPNET_DVR_TRANSDEVICE_STATUS = POINTER(struct_tagNET_DVR_TRANSDEVICE_STATUS)
tagNET_DVR_TRANSDEVICE_STATUS = struct_tagNET_DVR_TRANSDEVICE_STATUS
