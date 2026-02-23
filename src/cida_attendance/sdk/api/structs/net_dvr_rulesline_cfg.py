from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR


class struct_tagNET_DVR_RULESLINE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RULESLINE_CFG, [
    ('struRGB', NET_DVR_RGB_COLOR),
    ('byRes', BYTE * 128),
])

NET_DVR_RULESLINE_CFG = struct_tagNET_DVR_RULESLINE_CFG
LPNET_DVR_RULESLINE_CFG = POINTER(struct_tagNET_DVR_RULESLINE_CFG)
tagNET_DVR_RULESLINE_CFG = struct_tagNET_DVR_RULESLINE_CFG
