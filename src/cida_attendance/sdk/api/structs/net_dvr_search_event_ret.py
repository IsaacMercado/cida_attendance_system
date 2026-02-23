from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_270 import union_anon_270


class struct_tagNET_DVR_SEARCH_EVENT_RET(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_RET, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byChan', BYTE * int((32 + 32))),
    ('byChanEx', BYTE * 32),
    ('byRes', BYTE * 4),
    ('uSeniorRet', union_anon_270),
])

NET_DVR_SEARCH_EVENT_RET = struct_tagNET_DVR_SEARCH_EVENT_RET
LPNET_DVR_SEARCH_EVENT_RET = POINTER(struct_tagNET_DVR_SEARCH_EVENT_RET)
tagNET_DVR_SEARCH_EVENT_RET = struct_tagNET_DVR_SEARCH_EVENT_RET
