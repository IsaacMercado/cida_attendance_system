from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNet_DVR_PLAY_BACK_BY_TIME(Structure):
    pass

_S(struct_tagNet_DVR_PLAY_BACK_BY_TIME, [
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
])

NET_DVR_PLAY_BACK_BY_TIME = struct_tagNet_DVR_PLAY_BACK_BY_TIME
LPNET_DVR_PLAY_BACK_BY_TIME = POINTER(struct_tagNet_DVR_PLAY_BACK_BY_TIME)
tagNet_DVR_PLAY_BACK_BY_TIME = struct_tagNet_DVR_PLAY_BACK_BY_TIME
