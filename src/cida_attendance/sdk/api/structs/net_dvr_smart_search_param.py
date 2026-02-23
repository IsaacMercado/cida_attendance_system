from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_area_smartsearch_cond_union import NET_DVR_AREA_SMARTSEARCH_COND_UNION


class struct_tagNET_DVR_SMART_SEARCH_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SMART_SEARCH_PARAM, [
    ('byChan', BYTE),
    ('bySearchCondType', BYTE),
    ('wChan', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('uSmartSearchCond', NET_DVR_AREA_SMARTSEARCH_COND_UNION),
    ('bySensitivity', BYTE),
    ('byRes2', BYTE * 11),
])

NET_DVR_SMART_SEARCH_PARAM = struct_tagNET_DVR_SMART_SEARCH_PARAM
LPNET_DVR_SMART_SEARCH_PARAM = POINTER(struct_tagNET_DVR_SMART_SEARCH_PARAM)
tagNET_DVR_SMART_SEARCH_PARAM = struct_tagNET_DVR_SMART_SEARCH_PARAM
