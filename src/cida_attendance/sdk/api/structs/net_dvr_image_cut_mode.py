from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IMAGE_CUT_MODE(Structure):
    pass

_S(struct_tagNET_DVR_IMAGE_CUT_MODE, [
    ('dwSize', DWORD),
    ('byCutMode', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_IMAGE_CUT_MODE = struct_tagNET_DVR_IMAGE_CUT_MODE
LPNET_DVR_IMAGE_CUT_MODE = POINTER(struct_tagNET_DVR_IMAGE_CUT_MODE)
tagNET_DVR_IMAGE_CUT_MODE = struct_tagNET_DVR_IMAGE_CUT_MODE
