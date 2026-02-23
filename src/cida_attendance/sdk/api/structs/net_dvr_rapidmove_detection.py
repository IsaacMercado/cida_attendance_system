from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rapidmove_region import NET_DVR_RAPIDMOVE_REGION


class struct_tagNET_DVR_RAPIDMOVE_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_RAPIDMOVE_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struRegion', NET_DVR_RAPIDMOVE_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_RAPIDMOVE_DETECTION = struct_tagNET_DVR_RAPIDMOVE_DETECTION
LPNET_DVR_RAPIDMOVE_DETECTION = POINTER(struct_tagNET_DVR_RAPIDMOVE_DETECTION)
tagNET_DVR_RAPIDMOVE_DETECTION = struct_tagNET_DVR_RAPIDMOVE_DETECTION
