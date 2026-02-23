from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_PIC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PIC_INFO, [
    ('byPicType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPicWidth', DWORD),
    ('dwPicHeight', DWORD),
    ('dwPicDataLen', DWORD),
    ('byPicDataBuff', String),
    ('byRes2', BYTE * 32),
])

NET_DVR_PIC_INFO = struct_tagNET_DVR_PIC_INFO
LPNET_DVR_PIC_INFO = POINTER(struct_tagNET_DVR_PIC_INFO)
tagNET_DVR_PIC_INFO = struct_tagNET_DVR_PIC_INFO
