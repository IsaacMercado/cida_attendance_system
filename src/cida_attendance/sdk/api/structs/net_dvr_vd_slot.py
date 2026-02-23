from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VD_SLOT(Structure):
    pass

_S(struct_tagNET_DVR_VD_SLOT, [
    ('wVDSlot', WORD),
    ('byAlloc', BYTE),
    ('byRes', BYTE * 5),
    ('dwHVDSlotSize', DWORD),
    ('dwLVDSlotSize', DWORD),
])

NET_DVR_VD_SLOT = struct_tagNET_DVR_VD_SLOT
LPNET_DVR_VD_SLOT = POINTER(struct_tagNET_DVR_VD_SLOT)
tagNET_DVR_VD_SLOT = struct_tagNET_DVR_VD_SLOT
