from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PIC(Structure):
    pass

_S(struct_tagNET_DVR_PIC, [
    ('byPicType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPicWidth', DWORD),
    ('dwPicHeight', DWORD),
    ('dwPicDataLen', DWORD),
    ('dwPicDataBuffLen', DWORD),
    ('byPicDataBuff', POINTER(BYTE)),
    ('byRes2', BYTE * 40),
])

NET_DVR_PIC = struct_tagNET_DVR_PIC
LPNET_DVR_PIC = POINTER(struct_tagNET_DVR_PIC)
tagNET_DVR_PIC = struct_tagNET_DVR_PIC
