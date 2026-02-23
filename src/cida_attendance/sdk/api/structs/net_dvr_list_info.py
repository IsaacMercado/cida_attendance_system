from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LIST_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LIST_INFO, [
    ('dwSize', DWORD),
    ('byIndex', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LIST_INFO = struct_tagNET_DVR_LIST_INFO
LPNET_DVR_LIST_INFO = POINTER(struct_tagNET_DVR_LIST_INFO)
tagNET_DVR_LIST_INFO = struct_tagNET_DVR_LIST_INFO
