from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKGROUND_PIC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BACKGROUND_PIC_INFO, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byPicID', BYTE * 128),
    ('byRes', BYTE * 300),
])

NET_DVR_BACKGROUND_PIC_INFO = struct_tagNET_DVR_BACKGROUND_PIC_INFO
LPNET_DVR_BACKGROUND_PIC_INFO = POINTER(struct_tagNET_DVR_BACKGROUND_PIC_INFO)
tagNET_DVR_BACKGROUND_PIC_INFO = struct_tagNET_DVR_BACKGROUND_PIC_INFO
