from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_LOCK_PERCENTAGE(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_LOCK_PERCENTAGE, [
    ('dwSize', DWORD),
    ('byPercentage', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_RECORD_LOCK_PERCENTAGE = struct_tagNET_DVR_RECORD_LOCK_PERCENTAGE
LPNET_DVR_RECORD_LOCK_PERCENTAGE = POINTER(struct_tagNET_DVR_RECORD_LOCK_PERCENTAGE)
tagNET_DVR_RECORD_LOCK_PERCENTAGE = struct_tagNET_DVR_RECORD_LOCK_PERCENTAGE
