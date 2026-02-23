from ctypes import Structure

from ..base_classes import _S, LONG
from ..ctypes_preamble import POINTER, String
from .anon_199 import NET_DVR_DISPLAY_PARA


class struct_anon_200(Structure):
    pass

_S(struct_anon_200, [
    ('lChannel', LONG),
    ('lLinkMode', LONG),
    ('sMultiCastIP', String),
    ('struDisplayPara', NET_DVR_DISPLAY_PARA),
])

NET_DVR_CARDINFO = struct_anon_200
LPNET_DVR_CARDINFO = POINTER(struct_anon_200)
