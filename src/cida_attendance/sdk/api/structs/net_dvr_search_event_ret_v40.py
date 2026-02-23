from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_277 import union_anon_277


class struct_tagNET_DVR_SEARCH_EVENT_RET_V40(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_RET_V40, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('wChan', WORD * 512),
    ('byRes', BYTE * 36),
    ('uSeniorRet', union_anon_277),
])

NET_DVR_SEARCH_EVENT_RET_V40 = struct_tagNET_DVR_SEARCH_EVENT_RET_V40
LPNET_DVR_SEARCH_EVENT_RET_V40 = POINTER(struct_tagNET_DVR_SEARCH_EVENT_RET_V40)
tagNET_DVR_SEARCH_EVENT_RET_V40 = struct_tagNET_DVR_SEARCH_EVENT_RET_V40
