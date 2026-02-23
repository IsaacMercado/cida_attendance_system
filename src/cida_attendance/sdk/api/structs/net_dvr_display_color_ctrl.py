from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPLAY_COLOR_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAY_COLOR_CTRL, [
    ('byColorType', BYTE),
    ('byScale', c_char),
    ('byRes', BYTE * 14),
])

NET_DVR_DISPLAY_COLOR_CTRL = struct_tagNET_DVR_DISPLAY_COLOR_CTRL
LPNET_DVR_DISPLAY_COLOR_CTRL = POINTER(struct_tagNET_DVR_DISPLAY_COLOR_CTRL)
tagNET_DVR_DISPLAY_COLOR_CTRL = struct_tagNET_DVR_DISPLAY_COLOR_CTRL
