from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WININDEX_INFO(Structure):
    pass

_S(struct_tagNET_DVR_WININDEX_INFO, [
    ('dwWinIndex', DWORD),
    ('dwSubWinIndex', DWORD),
    ('byType', BYTE),
    ('byWallNo', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_WININDEX_INFO = struct_tagNET_DVR_WININDEX_INFO
LPNET_DVR_WININDEX_INFO = POINTER(struct_tagNET_DVR_WININDEX_INFO)
tagNET_DVR_WININDEX_INFO = struct_tagNET_DVR_WININDEX_INFO
