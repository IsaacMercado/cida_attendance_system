from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVICE_BOARD_EXCEPINFO(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_BOARD_EXCEPINFO, [
    ('dwSize', DWORD),
    ('byExceptNum', BYTE),
    ('byRes1', BYTE * 3),
    ('byMajor', BYTE * 16),
    ('wMinor', WORD * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_DEVICE_BOARD_EXCEPINFO = struct_tagNET_DVR_DEVICE_BOARD_EXCEPINFO
LPNET_DVR_DEVICE_BOARD_EXCEPINFO = POINTER(struct_tagNET_DVR_DEVICE_BOARD_EXCEPINFO)
tagNET_DVR_DEVICE_BOARD_EXCEPINFO = struct_tagNET_DVR_DEVICE_BOARD_EXCEPINFO
