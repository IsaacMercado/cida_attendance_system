from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALLWIN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_WALLWIN_INFO, [
    ('dwSize', DWORD),
    ('dwWinNum', DWORD),
    ('dwSubWinNum', DWORD),
    ('dwWallNo', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_WALLWIN_INFO = struct_tagNET_DVR_WALLWIN_INFO
LPNET_DVR_WALLWIN_INFO = POINTER(struct_tagNET_DVR_WALLWIN_INFO)
tagNET_DVR_WALLWIN_INFO = struct_tagNET_DVR_WALLWIN_INFO
