from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_pic_feature_union import NET_DVR_PIC_FEATURE_UNION
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_SMART_SEARCH_PIC_RET(Structure):
    pass

_S(struct_tagNET_DVR_SMART_SEARCH_PIC_RET, [
    ('sFileName', c_char * 64),
    ('struTime', NET_DVR_TIME_EX),
    ('dwFileSize', DWORD),
    ('wPicType', WORD),
    ('byRes1', BYTE * 2),
    ('uPicFeature', NET_DVR_PIC_FEATURE_UNION),
    ('byISO8601', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 29),
])

NET_DVR_SMART_SEARCH_PIC_RET = struct_tagNET_DVR_SMART_SEARCH_PIC_RET
LPNET_DVR_SMART_SEARCH_PIC_RET = POINTER(struct_tagNET_DVR_SMART_SEARCH_PIC_RET)
tagNET_DVR_SMART_SEARCH_PIC_RET = struct_tagNET_DVR_SMART_SEARCH_PIC_RET
