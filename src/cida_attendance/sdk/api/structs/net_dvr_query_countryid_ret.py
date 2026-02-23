from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_COUNTRYID_RET(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_COUNTRYID_RET, [
    ('szResolveSvrAddr', c_char * 64),
    ('szAlarmSvrAddr', c_char * 64),
    ('byRes', BYTE * 1024),
])

NET_DVR_QUERY_COUNTRYID_RET = struct_tagNET_DVR_QUERY_COUNTRYID_RET
LPNET_DVR_QUERY_COUNTRYID_RET = POINTER(struct_tagNET_DVR_QUERY_COUNTRYID_RET)
tagNET_DVR_QUERY_COUNTRYID_RET = struct_tagNET_DVR_QUERY_COUNTRYID_RET
