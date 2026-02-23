from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TV_SCREEN_COND(Structure):
    pass

_S(struct_tagNET_DVR_TV_SCREEN_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('wTVScreenNo', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_TV_SCREEN_COND = struct_tagNET_DVR_TV_SCREEN_COND
LPNET_DVR_TV_SCREEN_COND = POINTER(struct_tagNET_DVR_TV_SCREEN_COND)
tagNET_DVR_TV_SCREEN_COND = struct_tagNET_DVR_TV_SCREEN_COND
