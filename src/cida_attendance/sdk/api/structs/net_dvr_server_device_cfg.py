from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SERVER_DEVICE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SERVER_DEVICE_CFG, [
    ('byDeviceName', BYTE * 32),
    ('byDeviceType', BYTE),
    ('byDeviceID', BYTE),
    ('byLockNum', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_SERVER_DEVICE_CFG = struct_tagNET_DVR_SERVER_DEVICE_CFG
LPNET_DVR_SERVER_DEVICE_CFG = POINTER(struct_tagNET_DVR_SERVER_DEVICE_CFG)
tagNET_DVR_SERVER_DEVICE_CFG = struct_tagNET_DVR_SERVER_DEVICE_CFG
