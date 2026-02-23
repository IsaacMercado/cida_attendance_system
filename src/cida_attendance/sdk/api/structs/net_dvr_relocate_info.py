from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RELOCATE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_RELOCATE_INFO, [
    ('dwSize', DWORD),
    ('byTakeOverAddr', BYTE * 64),
    ('wPort', WORD),
    ('byRes', BYTE * 254),
])

NET_DVR_RELOCATE_INFO = struct_tagNET_DVR_RELOCATE_INFO
LPNET_DVR_RELOCATE_INFO = POINTER(struct_tagNET_DVR_RELOCATE_INFO)
tagNET_DVR_RELOCATE_INFO = struct_tagNET_DVR_RELOCATE_INFO
