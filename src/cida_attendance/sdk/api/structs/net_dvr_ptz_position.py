from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_186 import NET_DVR_PTZPOS


class struct_tagNET_DVR_PTZ_POSITION(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_POSITION, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byPtzPositionName', BYTE * 32),
    ('struPtzPos', NET_DVR_PTZPOS),
    ('byRes2', BYTE * 40),
])

NET_DVR_PTZ_POSITION = struct_tagNET_DVR_PTZ_POSITION
LPNET_DVR_PTZ_POSITION = POINTER(struct_tagNET_DVR_PTZ_POSITION)
tagNET_DVR_PTZ_POSITION = struct_tagNET_DVR_PTZ_POSITION
