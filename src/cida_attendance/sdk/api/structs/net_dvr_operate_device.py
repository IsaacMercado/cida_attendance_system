from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPERATE_DEVICE(Structure):
    pass

_S(struct_tagNET_DVR_OPERATE_DEVICE, [
    ('dwSize', DWORD),
    ('dwSubCommand', DWORD),
    ('dwDeviceIndex', DWORD),
    ('byRes', BYTE * 44),
])

NET_DVR_OPERATE_DEVICE = struct_tagNET_DVR_OPERATE_DEVICE
LPNET_DVR_OPERATE_DEVICE = POINTER(struct_tagNET_DVR_OPERATE_DEVICE)
tagNET_DVR_OPERATE_DEVICE = struct_tagNET_DVR_OPERATE_DEVICE
