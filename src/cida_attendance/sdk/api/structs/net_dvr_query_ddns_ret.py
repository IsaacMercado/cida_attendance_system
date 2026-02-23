from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_DDNS_RET(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_DDNS_RET, [
    ('szDevIP', c_char * 48),
    ('wCmdPort', WORD),
    ('wHttpPort', WORD),
    ('byRes', BYTE * 460),
])

NET_DVR_QUERY_DDNS_RET = struct_tagNET_DVR_QUERY_DDNS_RET
LPNET_DVR_QUERY_DDNS_RET = POINTER(struct_tagNET_DVR_QUERY_DDNS_RET)
tagNET_DVR_QUERY_DDNS_RET = struct_tagNET_DVR_QUERY_DDNS_RET
