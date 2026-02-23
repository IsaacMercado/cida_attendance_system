from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_242 import union_anon_242


class struct_tagNET_DVR_SEARCH_EVENT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_PARAM, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byLockType', BYTE),
    ('byValue', BYTE),
    ('byRes', BYTE * 130),
    ('uSeniorParam', union_anon_242),
])

NET_DVR_SEARCH_EVENT_PARAM = struct_tagNET_DVR_SEARCH_EVENT_PARAM
LPNET_DVR_SEARCH_EVENT_PARAM = POINTER(struct_tagNET_DVR_SEARCH_EVENT_PARAM)
tagNET_DVR_SEARCH_EVENT_PARAM = struct_tagNET_DVR_SEARCH_EVENT_PARAM
