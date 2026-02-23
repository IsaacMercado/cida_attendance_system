from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECTCFG(Structure):
    pass

_S(struct_tagNET_DVR_RECTCFG, [
    ('wXCoordinate', WORD),
    ('wYCoordinate', WORD),
    ('wWidth', WORD),
    ('wHeight', WORD),
])

NET_DVR_RECTCFG = struct_tagNET_DVR_RECTCFG
LPNET_DVR_RECTCFG = POINTER(struct_tagNET_DVR_RECTCFG)
tagNET_DVR_RECTCFG = struct_tagNET_DVR_RECTCFG
