from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_submatrixsysteminfo import NET_DVR_SUBMATRIXSYSTEMINFO


class struct_tagNET_DVR_UNITEDMATRIXSYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_UNITEDMATRIXSYSTEMINFO, [
    ('dwSize', DWORD),
    ('struMatrixInfo', NET_DVR_SUBMATRIXSYSTEMINFO * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_UNITEDMATRIXSYSTEMINFO = struct_tagNET_DVR_UNITEDMATRIXSYSTEMINFO
LPNET_DVR_UNITEDMATRIXSYSTEMINFO = POINTER(struct_tagNET_DVR_UNITEDMATRIXSYSTEMINFO)
tagNET_DVR_UNITEDMATRIXSYSTEMINFO = struct_tagNET_DVR_UNITEDMATRIXSYSTEMINFO
