from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_MATRIX_MONITORINFO(Structure):
    pass

_S(struct_tagNET_MATRIX_MONITORINFO, [
    ('dwGloalMonId', DWORD),
    ('sMonName', BYTE * 32),
    ('dwMatrixId', DWORD),
    ('dwLocalMonId', DWORD),
    ('byValid', BYTE),
    ('byTrunkType', BYTE),
    ('byUsedByTrunk', BYTE),
    ('byTrunkReq', BYTE),
    ('struInstallTime', NET_DVR_TIME),
    ('sPurpose', BYTE * 32),
    ('byRes', BYTE * 20),
])

NET_MATRIX_MONITORINFO = struct_tagNET_MATRIX_MONITORINFO
LPNET_MATRIX_MONITORINFO = POINTER(struct_tagNET_MATRIX_MONITORINFO)
tagNET_MATRIX_MONITORINFO = struct_tagNET_MATRIX_MONITORINFO
