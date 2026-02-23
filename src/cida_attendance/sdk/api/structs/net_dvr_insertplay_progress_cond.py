from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INSERTPLAY_PROGRESS_COND(Structure):
    pass

_S(struct_tagNET_DVR_INSERTPLAY_PROGRESS_COND, [
    ('dwSize', DWORD),
    ('byInsertType', BYTE),
    ('byRes3', BYTE * 3),
    ('dwInsertNo', DWORD),
    ('byProgressType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwGroupNo', DWORD),
    ('dwTerminalNo', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_INSERTPLAY_PROGRESS_COND = struct_tagNET_DVR_INSERTPLAY_PROGRESS_COND
LPNET_DVR_INSERTPLAY_PROGRESS_COND = POINTER(struct_tagNET_DVR_INSERTPLAY_PROGRESS_COND)
tagNET_DVR_INSERTPLAY_PROGRESS_COND = struct_tagNET_DVR_INSERTPLAY_PROGRESS_COND
