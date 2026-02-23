from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BARRIERGATE_COND(Structure):
    pass

_S(struct_tagNET_DVR_BARRIERGATE_COND, [
    ('byLaneNo', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_BARRIERGATE_COND = struct_tagNET_DVR_BARRIERGATE_COND
LPNET_DVR_BARRIERGATE_COND = POINTER(struct_tagNET_DVR_BARRIERGATE_COND)
tagNET_DVR_BARRIERGATE_COND = struct_tagNET_DVR_BARRIERGATE_COND
