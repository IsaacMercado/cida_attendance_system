from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_227 import union_anon_227


class struct_tagNET_DVR_TRACK_MODE(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_MODE, [
    ('dwSize', DWORD),
    ('byTrackMode', BYTE),
    ('byRuleConfMode', BYTE),
    ('byRes', BYTE * 2),
    ('uModeParam', union_anon_227),
])

NET_DVR_TRACK_MODE = struct_tagNET_DVR_TRACK_MODE
LPNET_DVR_TRACK_MODE = POINTER(struct_tagNET_DVR_TRACK_MODE)
tagNET_DVR_TRACK_MODE = struct_tagNET_DVR_TRACK_MODE
