from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DEVICEID_INFO(Structure):
    pass

_S(struct_tagNET_DEVICEID_INFO, [
    ('dwSize', DWORD),
    ('dwDeviceIndex', DWORD),
    ('byWallNo', BYTE),
    ('byRes1', BYTE * 27),
    ('dwChan', DWORD),
    ('dwInputSignalIndex', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_DEVICEID_INFO = struct_tagNET_DEVICEID_INFO
LPNET_DVR_DEVICEID_INFO = POINTER(struct_tagNET_DEVICEID_INFO)
tagNET_DEVICEID_INFO = struct_tagNET_DEVICEID_INFO
