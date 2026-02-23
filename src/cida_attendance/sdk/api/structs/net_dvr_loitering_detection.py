from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_loitering_region import NET_DVR_LOITERING_REGION


class struct_tagNET_DVR_LOITERING_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_LOITERING_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struRegion', NET_DVR_LOITERING_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_LOITERING_DETECTION = struct_tagNET_DVR_LOITERING_DETECTION
LPNET_DVR_LOITERING_DETECTION = POINTER(struct_tagNET_DVR_LOITERING_DETECTION)
tagNET_DVR_LOITERING_DETECTION = struct_tagNET_DVR_LOITERING_DETECTION
