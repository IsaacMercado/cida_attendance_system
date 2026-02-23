from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LINEARSCAN(Structure):
    pass

_S(struct_tagNET_DVR_LINEARSCAN, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byLinearScanType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LINEARSCAN = struct_tagNET_DVR_LINEARSCAN
LPNET_DVR_LINEARSCAN = POINTER(struct_tagNET_DVR_LINEARSCAN)
tagNET_DVR_LINEARSCAN = struct_tagNET_DVR_LINEARSCAN
