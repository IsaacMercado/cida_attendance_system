from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STORAGE_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_STORAGE_DETECTION, [
    ('dwSize', DWORD),
    ('byHealthState', BYTE),
    ('bySDCardState', BYTE),
    ('wAbnormalPowerLoss', WORD),
    ('wBadBlocks', WORD),
    ('byRemainingLife', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_STORAGE_DETECTION = struct_tagNET_DVR_STORAGE_DETECTION
LPNET_DVR_STORAGE_DETECTION = POINTER(struct_tagNET_DVR_STORAGE_DETECTION)
tagNET_DVR_STORAGE_DETECTION = struct_tagNET_DVR_STORAGE_DETECTION
