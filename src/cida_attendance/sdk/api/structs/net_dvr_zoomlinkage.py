from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ZOOMLINKAGE(Structure):
    pass

_S(struct_tagNET_DVR_ZOOMLINKAGE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_ZOOMLINKAGE = struct_tagNET_DVR_ZOOMLINKAGE
LPNET_DVR_ZOOMLINKAGE = POINTER(struct_tagNET_DVR_ZOOMLINKAGE)
tagNET_DVR_ZOOMLINKAGE = struct_tagNET_DVR_ZOOMLINKAGE
