from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_IPSERVER_COND(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_IPSERVER_COND, [
    ('szResolveSvrAddr', c_char * 64),
    ('wResolveSvrPort', WORD),
    ('szDevNickName', c_char * 64),
    ('szDevSerial', c_char * 48),
    ('byRes', BYTE * 334),
])

NET_DVR_QUERY_IPSERVER_COND = struct_tagNET_DVR_QUERY_IPSERVER_COND
LPNET_DVR_QUERY_IPSERVER_COND = POINTER(struct_tagNET_DVR_QUERY_IPSERVER_COND)
tagNET_DVR_QUERY_IPSERVER_COND = struct_tagNET_DVR_QUERY_IPSERVER_COND
