from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_groupdetection_region import NET_DVR_GROUPDETECTION_REGION


class struct_tagNET_DVR_GROUP_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_GROUP_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struRegion', NET_DVR_GROUPDETECTION_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_GROUP_DETECTION = struct_tagNET_DVR_GROUP_DETECTION
LPNET_DVR_GROUP_DETECTION = POINTER(struct_tagNET_DVR_GROUP_DETECTION)
tagNET_DVR_GROUP_DETECTION = struct_tagNET_DVR_GROUP_DETECTION
