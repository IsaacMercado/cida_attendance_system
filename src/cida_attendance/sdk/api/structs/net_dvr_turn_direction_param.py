from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TURN_DIRECTION_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TURN_DIRECTION_PARAM, [
    ('byLine', BYTE),
    ('byStatus', BYTE),
    ('byRes', BYTE * 38),
])

NET_DVR_TURN_DIRECTION_PARAM = struct_tagNET_DVR_TURN_DIRECTION_PARAM
LPNET_DVR_TURN_DIRECTION_PARAM = POINTER(struct_tagNET_DVR_TURN_DIRECTION_PARAM)
tagNET_DVR_TURN_DIRECTION_PARAM = struct_tagNET_DVR_TURN_DIRECTION_PARAM
