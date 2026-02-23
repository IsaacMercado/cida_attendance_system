from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SUBBOARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SUBBOARD_INFO, [
    ('dwSize', DWORD),
    ('byBoardType', BYTE),
    ('byInterfaceNum', BYTE),
    ('byStatus', BYTE),
    ('bySyncStatus', BYTE),
    ('dwSlotNo', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_SUBBOARD_INFO = struct_tagNET_DVR_SUBBOARD_INFO
LPNET_DVR_SUBBOARD_INFO = POINTER(struct_tagNET_DVR_SUBBOARD_INFO)
tagNET_DVR_SUBBOARD_INFO = struct_tagNET_DVR_SUBBOARD_INFO
