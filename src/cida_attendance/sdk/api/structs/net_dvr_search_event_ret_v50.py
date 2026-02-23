from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_286 import union_anon_286
from .net_dvr_address import NET_DVR_ADDRESS
from .net_dvr_time_search import NET_DVR_TIME_SEARCH


class struct_tagNET_DVR_SEARCH_EVENT_RET_V50(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_RET_V50, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME_SEARCH),
    ('struEndTime', NET_DVR_TIME_SEARCH),
    ('struAddr', NET_DVR_ADDRESS),
    ('wChan', WORD * 512),
    ('byRes', BYTE * 256),
    ('uSeniorRet', union_anon_286),
])

NET_DVR_SEARCH_EVENT_RET_V50 = struct_tagNET_DVR_SEARCH_EVENT_RET_V50
LPNET_DVR_SEARCH_EVENT_RET_V50 = POINTER(struct_tagNET_DVR_SEARCH_EVENT_RET_V50)
tagNET_DVR_SEARCH_EVENT_RET_V50 = struct_tagNET_DVR_SEARCH_EVENT_RET_V50
