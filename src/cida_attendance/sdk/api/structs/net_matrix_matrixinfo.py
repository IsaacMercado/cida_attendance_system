from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_matrix_union import NET_MATRIX_UNION


class struct_tagNET_MATRIX_MATRIXINFO(Structure):
    pass

_S(struct_tagNET_MATRIX_MATRIXINFO, [
    ('dwSize', DWORD),
    ('dwMatrixId', DWORD),
    ('sDevName', BYTE * 32),
    ('byCtrlType', BYTE),
    ('byProtocolType', BYTE),
    ('byRes1', BYTE * 6),
    ('struMatrixUnion', NET_MATRIX_UNION),
    ('dwMaxPortsIn', DWORD),
    ('dwMaxPortsOut', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('struInstallTime', NET_DVR_TIME),
    ('sPurpose', BYTE * 32),
    ('byRes2', BYTE * 20),
])

NET_MATRIX_MATRIXINFO = struct_tagNET_MATRIX_MATRIXINFO
LPNET_MATRIX_MATRIXINFO = POINTER(struct_tagNET_MATRIX_MATRIXINFO)
tagNET_MATRIX_MATRIXINFO = struct_tagNET_MATRIX_MATRIXINFO
