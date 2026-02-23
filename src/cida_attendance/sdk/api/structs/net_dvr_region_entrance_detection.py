from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_regionentrance_region import NET_DVR_REGIONENTRANCE_REGION


class struct_tagNET_DVR_REGION_ENTRANCE_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_REGION_ENTRANCE_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byEnableHumanMisinfoFilter', BYTE),
    ('byEnableVehicleMisinfoFilter', BYTE),
    ('byRes1', BYTE * 1),
    ('struRegion', NET_DVR_REGIONENTRANCE_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_REGION_ENTRANCE_DETECTION = struct_tagNET_DVR_REGION_ENTRANCE_DETECTION
LPNET_DVR_REGION_ENTRANCE_DETECTION = POINTER(struct_tagNET_DVR_REGION_ENTRANCE_DETECTION)
tagNET_DVR_REGION_ENTRANCE_DETECTION = struct_tagNET_DVR_REGION_ENTRANCE_DETECTION
