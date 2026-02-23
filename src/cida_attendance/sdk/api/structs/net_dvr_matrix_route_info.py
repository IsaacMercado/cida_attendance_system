from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_ROUTE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_ROUTE_INFO, [
    ('dwSize', DWORD),
    ('dwCamNo', DWORD),
    ('dwMonNo', DWORD),
    ('dwSubWin', DWORD),
    ('dwUserId', DWORD),
    ('dwTrunkId', DWORD * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_MATRIX_ROUTE_INFO = struct_tagNET_DVR_MATRIX_ROUTE_INFO
LPNET_DVR_MATRIX_ROUTE_INFO = POINTER(struct_tagNET_DVR_MATRIX_ROUTE_INFO)
tagNET_DVR_MATRIX_ROUTE_INFO = struct_tagNET_DVR_MATRIX_ROUTE_INFO
