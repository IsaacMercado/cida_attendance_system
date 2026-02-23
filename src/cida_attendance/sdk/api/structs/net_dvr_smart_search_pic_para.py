from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_smartsearch_pic_union import NET_DVR_SMARTSEARCH_PIC_UNION
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_SMART_SEARCH_PIC_PARA(Structure):
    pass

_S(struct_tagNET_DVR_SMART_SEARCH_PIC_PARA, [
    ('dwChanNo', DWORD),
    ('byStreamID', DWORD * 32),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('wSearchType', WORD),
    ('byRes1', BYTE * 2),
    ('uSmartSearchCond', NET_DVR_SMARTSEARCH_PIC_UNION),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes', BYTE * 59),
])

NET_DVR_SMART_SEARCH_PIC_PARA = struct_tagNET_DVR_SMART_SEARCH_PIC_PARA
LPNET_DVR_SMART_SEARCH_PIC_PARA = POINTER(struct_tagNET_DVR_SMART_SEARCH_PIC_PARA)
tagNET_DVR_SMART_SEARCH_PIC_PARA = struct_tagNET_DVR_SMART_SEARCH_PIC_PARA
