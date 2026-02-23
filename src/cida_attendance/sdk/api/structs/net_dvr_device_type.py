from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVICE_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_TYPE, [
    ('dwType', DWORD),
    ('byDescribe', BYTE * 16),
])

NET_DVR_DEVICE_TYPE = struct_tagNET_DVR_DEVICE_TYPE
LPNET_DVR_DEVICE_TYPE = POINTER(struct_tagNET_DVR_DEVICE_TYPE)
tagNET_DVR_DEVICE_TYPE = struct_tagNET_DVR_DEVICE_TYPE
