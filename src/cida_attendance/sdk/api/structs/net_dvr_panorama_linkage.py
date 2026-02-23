from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PANORAMA_LINKAGE(Structure):
    pass

_S(struct_tagNET_DVR_PANORAMA_LINKAGE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_PANORAMA_LINKAGE = struct_tagNET_DVR_PANORAMA_LINKAGE
LPNET_DVR_PANORAMA_LINKAGE = POINTER(struct_tagNET_DVR_PANORAMA_LINKAGE)
tagNET_DVR_PANORAMA_LINKAGE = struct_tagNET_DVR_PANORAMA_LINKAGE
