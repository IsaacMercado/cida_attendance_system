from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPTICAL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_INFO, [
    ('dwSize', DWORD),
    ('bySlotNum', BYTE),
    ('byChannel', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_OPTICAL_INFO = struct_tagNET_DVR_OPTICAL_INFO
LPNET_DVR_OPTICAL_INFO = POINTER(struct_tagNET_DVR_OPTICAL_INFO)
tagNET_DVR_OPTICAL_INFO = struct_tagNET_DVR_OPTICAL_INFO
