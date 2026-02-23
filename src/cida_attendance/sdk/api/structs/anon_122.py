from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_121 import NET_DVR_DECCHANINFO


class struct_anon_122(Structure):
    pass

_S(struct_anon_122, [
    ('byPoolChans', BYTE),
    ('struchanConInfo', NET_DVR_DECCHANINFO * 4),
    ('byEnablePoll', BYTE),
    ('byPoolTime', BYTE),
])

NET_DVR_DECINFO = struct_anon_122
LPNET_DVR_DECINFO = POINTER(struct_anon_122)
