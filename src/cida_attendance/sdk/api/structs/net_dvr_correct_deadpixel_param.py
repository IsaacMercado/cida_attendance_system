from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CORRECT_DEADPIXEL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CORRECT_DEADPIXEL_PARAM, [
    ('dwSize', DWORD),
    ('dwCommand', DWORD),
    ('dwDeadPixelX', DWORD),
    ('dwDeadPixelY', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_CORRECT_DEADPIXEL_PARAM = struct_tagNET_DVR_CORRECT_DEADPIXEL_PARAM
LPNET_DVR_CORRECT_DEADPIXEL_PARAM = POINTER(struct_tagNET_DVR_CORRECT_DEADPIXEL_PARAM)
tagNET_DVR_CORRECT_DEADPIXEL_PARAM = struct_tagNET_DVR_CORRECT_DEADPIXEL_PARAM
