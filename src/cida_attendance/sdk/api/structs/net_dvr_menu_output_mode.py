from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MENU_OUTPUT_MODE(Structure):
    pass

_S(struct_tagNET_DVR_MENU_OUTPUT_MODE, [
    ('dwSize', DWORD),
    ('byMenuOutputMode', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_MENU_OUTPUT_MODE = struct_tagNET_DVR_MENU_OUTPUT_MODE
LPNET_DVR_MENU_OUTPUT_MODE = POINTER(struct_tagNET_DVR_MENU_OUTPUT_MODE)
tagNET_DVR_MENU_OUTPUT_MODE = struct_tagNET_DVR_MENU_OUTPUT_MODE
