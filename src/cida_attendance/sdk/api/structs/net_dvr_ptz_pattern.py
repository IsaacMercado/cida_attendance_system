from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_PATTERN(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_PATTERN, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwPatternCmd', DWORD),
    ('dwPatternID', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_PTZ_PATTERN = struct_tagNET_DVR_PTZ_PATTERN
LPNET_DVR_PTZ_PATTERN = POINTER(struct_tagNET_DVR_PTZ_PATTERN)
tagNET_DVR_PTZ_PATTERN = struct_tagNET_DVR_PTZ_PATTERN
