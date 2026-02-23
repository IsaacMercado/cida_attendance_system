from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_submatrixinfo import NET_DVR_SUBMATRIXINFO


class struct_tagNET_DVR_ALLUNITEDMATRIXINFO(Structure):
    pass

_S(struct_tagNET_DVR_ALLUNITEDMATRIXINFO, [
    ('dwSize', DWORD),
    ('struSubMatrixInfo', NET_DVR_SUBMATRIXINFO * 8),
    ('byRes2', BYTE * 32),
])

NET_DVR_ALLUNITEDMATRIXINFO = struct_tagNET_DVR_ALLUNITEDMATRIXINFO
LPNET_DVR_ALLUNITEDMATRIXINFO = POINTER(struct_tagNET_DVR_ALLUNITEDMATRIXINFO)
tagNET_DVR_ALLUNITEDMATRIXINFO = struct_tagNET_DVR_ALLUNITEDMATRIXINFO
