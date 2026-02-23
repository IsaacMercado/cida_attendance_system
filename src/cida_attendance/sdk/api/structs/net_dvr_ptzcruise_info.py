from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZCRUISE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PTZCRUISE_INFO, [
    ('dwSize', DWORD),
    ('dwPtzCruiseNum', DWORD),
    ('dwGroupNum', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_PTZCRUISE_INFO = struct_tagNET_DVR_PTZCRUISE_INFO
LPNET_DVR_PTZCRUISE_INFO = POINTER(struct_tagNET_DVR_PTZCRUISE_INFO)
tagNET_DVR_PTZCRUISE_INFO = struct_tagNET_DVR_PTZCRUISE_INFO
