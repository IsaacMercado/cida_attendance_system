from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AGING_TRICK_SCAN(Structure):
    pass

_S(struct_tagNET_DVR_AGING_TRICK_SCAN, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byAging', BYTE),
    ('byWriteReadEnalbe', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_AGING_TRICK_SCAN = struct_tagNET_DVR_AGING_TRICK_SCAN
LPNET_DVR_AGING_TRICK_SCAN = POINTER(struct_tagNET_DVR_AGING_TRICK_SCAN)
tagNET_DVR_AGING_TRICK_SCAN = struct_tagNET_DVR_AGING_TRICK_SCAN
