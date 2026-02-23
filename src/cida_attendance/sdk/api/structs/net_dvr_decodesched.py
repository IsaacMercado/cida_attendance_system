from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG


class struct_tagNET_DVR_DECODESCHED(Structure):
    pass

_S(struct_tagNET_DVR_DECODESCHED, [
    ('struSchedTime', NET_DVR_SCHEDTIME),
    ('byDecodeType', BYTE),
    ('byLoopGroup', BYTE),
    ('byRes', BYTE * 6),
    ('struDynamicDec', NET_DVR_PU_STREAM_CFG),
])

NET_DVR_DECODESCHED = struct_tagNET_DVR_DECODESCHED
LPNET_DVR_DECODESCHED = POINTER(struct_tagNET_DVR_DECODESCHED)
tagNET_DVR_DECODESCHED = struct_tagNET_DVR_DECODESCHED
