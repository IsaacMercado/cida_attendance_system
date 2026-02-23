from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_regionexiting_region import NET_DVR_REGIONEXITING_REGION


class struct_tagNET_DVR_REGION_EXITING_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_REGION_EXITING_DETECTION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byEnableHumanMisinfoFilter', BYTE),
    ('byEnableVehicleMisinfoFilter', BYTE),
    ('byRes1', BYTE * 1),
    ('struRegion', NET_DVR_REGIONEXITING_REGION * 8),
    ('byRes2', BYTE * 128),
])

NET_DVR_REGION_EXITING_DETECTION = struct_tagNET_DVR_REGION_EXITING_DETECTION
LPNET_DVR_REGION_EXITING_DETECTION = POINTER(struct_tagNET_DVR_REGION_EXITING_DETECTION)
tagNET_DVR_REGION_EXITING_DETECTION = struct_tagNET_DVR_REGION_EXITING_DETECTION
