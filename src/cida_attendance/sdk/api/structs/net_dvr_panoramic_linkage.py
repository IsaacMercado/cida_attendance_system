from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PANORAMIC_LINKAGE(Structure):
    pass

_S(struct_tagNET_DVR_PANORAMIC_LINKAGE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byType', BYTE),
    ('byRes1', BYTE * 3),
    ('byMACAddr', BYTE * 6),
    ('byRes2', BYTE * 2),
    ('struDevIP', NET_DVR_IPADDR),
    ('dwPicLen', DWORD),
    ('pPicBuff', String),
    ('byRes', BYTE * 128),
])

NET_DVR_PANORAMIC_LINKAGE = struct_tagNET_DVR_PANORAMIC_LINKAGE
LPNET_DVR_PANORAMIC_LINKAGE = POINTER(struct_tagNET_DVR_PANORAMIC_LINKAGE)
tagNET_DVR_PANORAMIC_LINKAGE = struct_tagNET_DVR_PANORAMIC_LINKAGE
