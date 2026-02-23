from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_263 import union_anon_263
from .net_dvr_time_search_cond import NET_DVR_TIME_SEARCH_COND


class struct_tagNET_DVR_SEARCH_EVENT_PARAM_V50(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_EVENT_PARAM_V50, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME_SEARCH_COND),
    ('struEndTime', NET_DVR_TIME_SEARCH_COND),
    ('byLockType', BYTE),
    ('byQuickSearch', BYTE),
    ('byRes', BYTE * 254),
    ('uSeniorParam', union_anon_263),
])

NET_DVR_SEARCH_EVENT_PARAM_V50 = struct_tagNET_DVR_SEARCH_EVENT_PARAM_V50
LPNET_DVR_SEARCH_EVENT_PARAM_V50 = POINTER(struct_tagNET_DVR_SEARCH_EVENT_PARAM_V50)
tagNET_DVR_SEARCH_EVENT_PARAM_V50 = struct_tagNET_DVR_SEARCH_EVENT_PARAM_V50
