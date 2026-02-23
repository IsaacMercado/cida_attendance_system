from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPLAY_POSITION_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAY_POSITION_CTRL, [
    ('byPositionType', BYTE),
    ('byScale', c_char),
    ('byRes', BYTE * 14),
])

NET_DVR_DISPLAY_POSITION_CTRL = struct_tagNET_DVR_DISPLAY_POSITION_CTRL
LPNET_DVR_DISPLAY_POSITION_CTRL = POINTER(struct_tagNET_DVR_DISPLAY_POSITION_CTRL)
tagNET_DVR_DISPLAY_POSITION_CTRL = struct_tagNET_DVR_DISPLAY_POSITION_CTRL
