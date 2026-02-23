from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVICE_LAN_ENCODE(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_LAN_ENCODE, [
    ('dwSize', DWORD),
    ('byLanEncode', BYTE * 32),
    ('byRes', BYTE * 28),
])

NET_DVR_DEVICE_LAN_ENCODE = struct_tagNET_DVR_DEVICE_LAN_ENCODE
LPNET_DVR_DEVICE_LAN_ENCODE = POINTER(struct_tagNET_DVR_DEVICE_LAN_ENCODE)
tagNET_DVR_DEVICE_LAN_ENCODE = struct_tagNET_DVR_DEVICE_LAN_ENCODE
