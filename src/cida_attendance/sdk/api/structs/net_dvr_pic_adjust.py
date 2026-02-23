from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PIC_ADJUST(Structure):
    pass

_S(struct_tagNET_DVR_PIC_ADJUST, [
    ('dwSize', DWORD),
    ('bySubCommand', BYTE),
    ('byScale', BYTE),
    ('byPictureProportion', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_PIC_ADJUST = struct_tagNET_DVR_PIC_ADJUST
LPNET_DVR_PIC_ADJUST = POINTER(struct_tagNET_DVR_PIC_ADJUST)
tagNET_DVR_PIC_ADJUST = struct_tagNET_DVR_PIC_ADJUST
