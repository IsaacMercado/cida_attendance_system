from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_TIME_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_TIME_DETECTION, [
    ('struSchedTime', NET_DVR_SCHEDTIME),
    ('byDetSceneID', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_TIME_DETECTION = struct_tagNET_DVR_TIME_DETECTION
LPNET_DVR_TIME_DETECTION = POINTER(struct_tagNET_DVR_TIME_DETECTION)
tagNET_DVR_TIME_DETECTION = struct_tagNET_DVR_TIME_DETECTION
