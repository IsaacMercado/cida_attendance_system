from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_KEYBOARD_USER(Structure):
    pass

_S(struct_tagNET_DVR_KEYBOARD_USER, [
    ('dwSize', DWORD),
    ('dwID', DWORD),
    ('byDefanceArea', BYTE * 512),
    ('byRes', BYTE * 560),
])

NET_DVR_KEYBOARD_USER = struct_tagNET_DVR_KEYBOARD_USER
LPNET_DVR_KEYBOARD_USER = POINTER(struct_tagNET_DVR_KEYBOARD_USER)
tagNET_DVR_KEYBOARD_USER = struct_tagNET_DVR_KEYBOARD_USER
