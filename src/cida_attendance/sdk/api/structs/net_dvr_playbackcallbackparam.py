from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_330 import union_anon_330


class struct_tagNET_DVR_PLAYBACKCALLBACKPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PLAYBACKCALLBACKPARAM, [
    ('byPlayBackMode', BYTE),
    ('byRes1', BYTE * 3),
    ('playbackmode', union_anon_330),
    ('nSessionID', DWORD),
    ('byRes2', BYTE * 44),
])

NET_DVR_PLAYBACKCALLBACKPARAM = struct_tagNET_DVR_PLAYBACKCALLBACKPARAM
LPNET_DVR_PLAYBACKCALLBACKPARAM = POINTER(struct_tagNET_DVR_PLAYBACKCALLBACKPARAM)
tagNET_DVR_PLAYBACKCALLBACKPARAM = struct_tagNET_DVR_PLAYBACKCALLBACKPARAM
