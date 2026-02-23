from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_485LIST_INFO(Structure):
    pass

_S(struct_tagNET_DVR_485LIST_INFO, [
    ('dwSize', DWORD),
    ('byAll', BYTE),
    ('byres', BYTE * 3),
    ('byIndex', BYTE * 256),
    ('byRes', BYTE * 64),
])

NET_DVR_485LIST_INFO = struct_tagNET_DVR_485LIST_INFO
LPNET_DVR_485LIST_INFO = POINTER(struct_tagNET_DVR_485LIST_INFO)
tagNET_DVR_485LIST_INFO = struct_tagNET_DVR_485LIST_INFO
