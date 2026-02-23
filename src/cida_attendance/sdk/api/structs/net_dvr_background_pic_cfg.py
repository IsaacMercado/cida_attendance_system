from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKGROUND_PIC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BACKGROUND_PIC_CFG, [
    ('dwSize', DWORD),
    ('dwPicSize', DWORD),
    ('dwPicType', DWORD),
    ('wPicWidth', WORD),
    ('wPicHeight', WORD),
    ('byPicName', BYTE * 128),
    ('byRes', BYTE * 128),
])

NET_DVR_BACKGROUND_PIC_CFG = struct_tagNET_DVR_BACKGROUND_PIC_CFG
LPNET_DVR_BACKGROUND_PIC_CFG = POINTER(struct_tagNET_DVR_BACKGROUND_PIC_CFG)
tagNET_DVR_BACKGROUND_PIC_CFG = struct_tagNET_DVR_BACKGROUND_PIC_CFG
