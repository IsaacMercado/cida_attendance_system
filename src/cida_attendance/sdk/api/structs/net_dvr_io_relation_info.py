from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IO_RELATION_INFO(Structure):
    pass

_S(struct_tagNET_DVR_IO_RELATION_INFO, [
    ('dwSize', DWORD),
    ('dwIORelation', DWORD * 256),
    ('byRes', BYTE * 256),
])

NET_DVR_IO_RELATION_INFO = struct_tagNET_DVR_IO_RELATION_INFO
LPNET_DVR_IO_RELATION_INFO = POINTER(struct_tagNET_DVR_IO_RELATION_INFO)
tagNET_DVR_IO_RELATION_INFO = struct_tagNET_DVR_IO_RELATION_INFO
