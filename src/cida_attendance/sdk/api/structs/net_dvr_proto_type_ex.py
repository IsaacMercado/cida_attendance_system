from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_tagNET_DVR_PROTO_TYPE_EX(Structure):
    pass

_S(struct_tagNET_DVR_PROTO_TYPE_EX, [
    ('wType', WORD),
    ('wCommunitionType', WORD),
    ('byDescribe', BYTE * 16),
])

NET_DVR_PROTO_TYPE_EX = struct_tagNET_DVR_PROTO_TYPE_EX
LPNET_DVR_PROTO_TYPE_EX = struct_tagNET_DVR_PROTO_TYPE_EX
tagNET_DVR_PROTO_TYPE_EX = struct_tagNET_DVR_PROTO_TYPE_EX
