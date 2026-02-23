from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKGROUND_PIC_PRARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKGROUND_PIC_PRARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwPicSize', DWORD),
    ('wPicWidth', WORD),
    ('wPicHeight', WORD),
    ('szPicName', c_char * 128),
    ('byPicType', BYTE),
    ('byRes', BYTE * 303),
])

NET_DVR_BACKGROUND_PIC_PRARAM = struct_tagNET_DVR_BACKGROUND_PIC_PRARAM
LPNET_DVR_BACKGROUND_PIC_PRARAM = POINTER(struct_tagNET_DVR_BACKGROUND_PIC_PRARAM)
tagNET_DVR_BACKGROUND_PIC_PRARAM = struct_tagNET_DVR_BACKGROUND_PIC_PRARAM
