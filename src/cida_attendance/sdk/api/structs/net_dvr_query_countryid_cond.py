from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_COUNTRYID_COND(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_COUNTRYID_COND, [
    ('wCountryID', WORD),
    ('szSvrAddr', c_char * 64),
    ('szClientVersion', c_char * 64),
    ('byRes', BYTE * 382),
])

NET_DVR_QUERY_COUNTRYID_COND = struct_tagNET_DVR_QUERY_COUNTRYID_COND
LPNET_DVR_QUERY_COUNTRYID_COND = POINTER(struct_tagNET_DVR_QUERY_COUNTRYID_COND)
tagNET_DVR_QUERY_COUNTRYID_COND = struct_tagNET_DVR_QUERY_COUNTRYID_COND
