from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKGROUND_PIC_COND(Structure):
    pass

_S(struct_tagNET_DVR_BACKGROUND_PIC_COND, [
    ('dwSize', DWORD),
    ('szFileID', c_char * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_BACKGROUND_PIC_COND = struct_tagNET_DVR_BACKGROUND_PIC_COND
LPNET_DVR_BACKGROUND_PIC_COND = POINTER(struct_tagNET_DVR_BACKGROUND_PIC_COND)
tagNET_DVR_BACKGROUND_PIC_COND = struct_tagNET_DVR_BACKGROUND_PIC_COND
