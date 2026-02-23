from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_SMART_SEARCH_RET(Structure):
    pass

_S(struct_tagNET_DVR_SMART_SEARCH_RET, [
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes', BYTE * 59),
])

NET_DVR_SMART_SEARCH_RET = struct_tagNET_DVR_SMART_SEARCH_RET
LPNET_DVR_SMART_SEARCH_RET = POINTER(struct_tagNET_DVR_SMART_SEARCH_RET)
tagNET_DVR_SMART_SEARCH_RET = struct_tagNET_DVR_SMART_SEARCH_RET
