from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEXTSHOW(Structure):
    pass

_S(struct_tagNET_DVR_TEXTSHOW, [
    ('dwSize', DWORD),
    ('byShowText', BYTE),
    ('byRes', BYTE * 35),
])

NET_DVR_TEXTSHOW = struct_tagNET_DVR_TEXTSHOW
LPNET_DVR_TEXTSHOW = POINTER(struct_tagNET_DVR_TEXTSHOW)
tagNET_DVR_TEXTSHOW = struct_tagNET_DVR_TEXTSHOW
