from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DESC_NODE(Structure):
    pass

_S(struct_tagNET_DVR_DESC_NODE, [
    ('iValue', c_int),
    ('byDescribe', BYTE * 32),
    ('dwFreeSpace', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_DESC_NODE = struct_tagNET_DVR_DESC_NODE
LPNET_DVR_DESC_NODE = POINTER(struct_tagNET_DVR_DESC_NODE)
tagNET_DVR_DESC_NODE = struct_tagNET_DVR_DESC_NODE
