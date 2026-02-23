from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ATM_PROTO_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PROTO_TYPE, [
    ('dwAtmType', DWORD),
    ('chDesc', c_char * 32),
])

NET_DVR_ATM_PROTO_TYPE = struct_tagNET_DVR_ATM_PROTO_TYPE
LPNET_DVR_ATM_PROTO_TYPE = POINTER(struct_tagNET_DVR_ATM_PROTO_TYPE)
tagNET_DVR_ATM_PROTO_TYPE = struct_tagNET_DVR_ATM_PROTO_TYPE
