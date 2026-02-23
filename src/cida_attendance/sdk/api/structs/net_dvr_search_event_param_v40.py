from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_252 import union_anon_252


class struct_tagNET_DVR_SEARCH_EVENT_PARAM_V40(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_PARAM_V40, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byLockType', BYTE),
    ('byQuickSearch', BYTE),
    ('byRes', BYTE * 130),
    ('uSeniorParam', union_anon_252),
])

NET_DVR_SEARCH_EVENT_PARAM_V40 = struct_tagNET_DVR_SEARCH_EVENT_PARAM_V40
LPNET_DVR_SEARCH_EVENT_PARAM_V40 = POINTER(struct_tagNET_DVR_SEARCH_EVENT_PARAM_V40)
tagNET_DVR_SEARCH_EVENT_PARAM_V40 = struct_tagNET_DVR_SEARCH_EVENT_PARAM_V40
