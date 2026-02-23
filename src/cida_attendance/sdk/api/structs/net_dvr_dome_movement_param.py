from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DOME_MOVEMENT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DOME_MOVEMENT_PARAM, [
    ('wMaxZoom', WORD),
    ('byRes', BYTE * 42),
])

NET_DVR_DOME_MOVEMENT_PARAM = struct_tagNET_DVR_DOME_MOVEMENT_PARAM
LPNET_DVR_DOME_MOVEMENT_PARAM = POINTER(struct_tagNET_DVR_DOME_MOVEMENT_PARAM)
tagNET_DVR_DOME_MOVEMENT_PARAM = struct_tagNET_DVR_DOME_MOVEMENT_PARAM
