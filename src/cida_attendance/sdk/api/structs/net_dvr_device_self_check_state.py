from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVICE_SELF_CHECK_STATE(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_SELF_CHECK_STATE, [
    ('dwSize', DWORD),
    ('dwRS485Chan', DWORD * 64),
    ('dwSensorChan', DWORD * 4),
    ('byRes', BYTE * 32),
])

NET_DVR_DEVICE_SELF_CHECK_STATE = struct_tagNET_DVR_DEVICE_SELF_CHECK_STATE
LPNET_DVR_DEVICE_SELF_CHECK_STATE = POINTER(struct_tagNET_DVR_DEVICE_SELF_CHECK_STATE)
tagNET_DVR_DEVICE_SELF_CHECK_STATE = struct_tagNET_DVR_DEVICE_SELF_CHECK_STATE
