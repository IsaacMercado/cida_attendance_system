from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_POINT(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_POINT, [
    ('wX', WORD),
    ('wY', WORD),
])

NET_DVR_SCREEN_POINT = struct_tagNET_DVR_SCREEN_POINT
LPNET_DVR_SCREEN_POINT = POINTER(struct_tagNET_DVR_SCREEN_POINT)
tagNET_DVR_SCREEN_POINT = struct_tagNET_DVR_SCREEN_POINT
