from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TOUCHPAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TOUCHPAD_PARAM, [
    ('byMouseEvent', BYTE),
    ('byRes1', BYTE * 3),
    ('iXDisplacement', c_int),
    ('iYDisplacement', c_int),
    ('byRes2', BYTE * 4),
])

NET_DVR_TOUCHPAD_PARAM = struct_tagNET_DVR_TOUCHPAD_PARAM
LPNET_DVR_TOUCHPAD_PARAM = POINTER(struct_tagNET_DVR_TOUCHPAD_PARAM)
tagNET_DVR_TOUCHPAD_PARAM = struct_tagNET_DVR_TOUCHPAD_PARAM
