from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_DDNS_COND(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_DDNS_COND, [
    ('szResolveSvrAddr', c_char * 64),
    ('szDevNickName', c_char * 64),
    ('szDevSerial', c_char * 48),
    ('szClientVersion', c_char * 64),
    ('byRes', BYTE * 272),
])

NET_DVR_QUERY_DDNS_COND = struct_tagNET_DVR_QUERY_DDNS_COND
LPNET_DVR_QUERY_DDNS_COND = POINTER(struct_tagNET_DVR_QUERY_DDNS_COND)
tagNET_DVR_QUERY_DDNS_COND = struct_tagNET_DVR_QUERY_DDNS_COND
