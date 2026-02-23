from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_IPSERVER_RET(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_IPSERVER_RET, [
    ('szDevIP', c_char * 48),
    ('wCmdPort', WORD),
    ('byRes', BYTE * 462),
])

NET_DVR_QUERY_IPSERVER_RET = struct_tagNET_DVR_QUERY_IPSERVER_RET
LPNET_DVR_QUERY_IPSERVER_RET = POINTER(struct_tagNET_DVR_QUERY_IPSERVER_RET)
tagNET_DVR_QUERY_IPSERVER_RET = struct_tagNET_DVR_QUERY_IPSERVER_RET
