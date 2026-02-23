from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPLAY_START_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAY_START_INFO, [
    ('dwSize', DWORD),
    ('dwDisplayChan', DWORD),
    ('dwCodeChan', DWORD),
    ('dwWinNum', DWORD),
    ('byEnableAudio', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_DISPLAY_START_INFO = struct_tagNET_DVR_DISPLAY_START_INFO
LPNET_DVR_DISPLAY_START_INFO = POINTER(struct_tagNET_DVR_DISPLAY_START_INFO)
tagNET_DVR_DISPLAY_START_INFO = struct_tagNET_DVR_DISPLAY_START_INFO
