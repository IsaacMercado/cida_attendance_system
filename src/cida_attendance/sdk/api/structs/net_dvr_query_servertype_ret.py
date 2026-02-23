from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_SERVERTYPE_RET(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_SERVERTYPE_RET, [
    ('szSvrAddr', c_char * 64),
    ('wSvrPort', WORD),
    ('byRes', BYTE * 446),
])

NET_DVR_QUERY_SERVERTYPE_RET = struct_tagNET_DVR_QUERY_SERVERTYPE_RET
LPNET_DVR_QUERY_SERVERTYPE_RET = POINTER(struct_tagNET_DVR_QUERY_SERVERTYPE_RET)
tagNET_DVR_QUERY_SERVERTYPE_RET = struct_tagNET_DVR_QUERY_SERVERTYPE_RET
