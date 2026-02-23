from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WINDOW_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_WINDOW_STATUS, [
    ('dwSize', DWORD),
    ('dwCodeChan', DWORD),
    ('byDisplay', BYTE),
    ('byAudio', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_WINDOW_STATUS = struct_tagNET_DVR_WINDOW_STATUS
LPNET_DVR_WINDOW_STATUS = POINTER(struct_tagNET_DVR_WINDOW_STATUS)
tagNET_DVR_WINDOW_STATUS = struct_tagNET_DVR_WINDOW_STATUS
