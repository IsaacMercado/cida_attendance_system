from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SPARTAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SPARTAN_INFO, [
    ('dwSize', DWORD),
    ('bySpartanStatus', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_SPARTAN_INFO = struct_tagNET_DVR_SPARTAN_INFO
LPNET_DVR_SPARTAN_INFO = POINTER(struct_tagNET_DVR_SPARTAN_INFO)
tagNET_DVR_SPARTAN_INFO = struct_tagNET_DVR_SPARTAN_INFO
