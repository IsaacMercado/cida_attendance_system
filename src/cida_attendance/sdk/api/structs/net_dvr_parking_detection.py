from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_parking_region import NET_DVR_PARKING_REGION


class struct_tagNET_DVR_PARKING_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_PARKING_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struRegion', NET_DVR_PARKING_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_PARKING_DETECTION = struct_tagNET_DVR_PARKING_DETECTION
LPNET_DVR_PARKING_DETECTION = POINTER(struct_tagNET_DVR_PARKING_DETECTION)
tagNET_DVR_PARKING_DETECTION = struct_tagNET_DVR_PARKING_DETECTION
