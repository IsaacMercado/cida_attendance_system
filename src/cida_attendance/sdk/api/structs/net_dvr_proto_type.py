from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PROTO_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_PROTO_TYPE, [
    ('dwType', DWORD),
    ('byDescribe', BYTE * 16),
])

NET_DVR_PROTO_TYPE = struct_tagNET_DVR_PROTO_TYPE
LPNET_DVR_PROTO_TYPE = POINTER(struct_tagNET_DVR_PROTO_TYPE)
tagNET_DVR_PROTO_TYPE = struct_tagNET_DVR_PROTO_TYPE
