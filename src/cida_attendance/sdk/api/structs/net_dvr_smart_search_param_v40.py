from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_area_smartsearch_cond_union import NET_DVR_AREA_SMARTSEARCH_COND_UNION
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_SMART_SEARCH_PARAM_V40(Structure):
    pass

_S(struct_tagNET_DVR_SMART_SEARCH_PARAM_V40, [
    ('dwSize', DWORD),
    ('struIDInfo', NET_DVR_STREAM_INFO),
    ('bySearchCondType', BYTE),
    ('bySensitivity', BYTE),
    ('byRes1', BYTE * 2),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('uSmartSearchCond', NET_DVR_AREA_SMARTSEARCH_COND_UNION),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes2', BYTE * 251),
])

NET_DVR_SMART_SEARCH_PARAM_V40 = struct_tagNET_DVR_SMART_SEARCH_PARAM_V40
LPNET_DVR_SMART_SEARCH_PARAM_V40 = POINTER(struct_tagNET_DVR_SMART_SEARCH_PARAM_V40)
tagNET_DVR_SMART_SEARCH_PARAM_V40 = struct_tagNET_DVR_SMART_SEARCH_PARAM_V40
