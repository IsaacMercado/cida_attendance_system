from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CODER_WINDOW_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CODER_WINDOW_INFO, [
    ('dwSize', DWORD),
    ('dwDisplayChan', DWORD),
    ('dwWinNum', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_CODER_WINDOW_INFO = struct_tagNET_DVR_CODER_WINDOW_INFO
LPNET_DVR_CODER_WINDOW_INFO = POINTER(struct_tagNET_DVR_CODER_WINDOW_INFO)
tagNET_DVR_CODER_WINDOW_INFO = struct_tagNET_DVR_CODER_WINDOW_INFO
