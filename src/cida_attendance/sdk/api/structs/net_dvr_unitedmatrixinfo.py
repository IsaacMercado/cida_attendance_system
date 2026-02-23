from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subserverinfo import NET_DVR_SUBSERVERINFO


class struct_tagNET_DVR_UNITEDMATRIXINFO(Structure):
    pass

_S(struct_tagNET_DVR_UNITEDMATRIXINFO, [
    ('dwSize', DWORD),
    ('struDomainInfo', NET_DVR_SUBSERVERINFO),
    ('struSubDomainInfo', NET_DVR_SUBSERVERINFO * 4),
    ('struMatrixInfo', NET_DVR_SUBSERVERINFO * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_UNITEDMATRIXINFO = struct_tagNET_DVR_UNITEDMATRIXINFO
LPNET_DVR_UNITEDMATRIXINFO = POINTER(struct_tagNET_DVR_UNITEDMATRIXINFO)
tagNET_DVR_UNITEDMATRIXINFO = struct_tagNET_DVR_UNITEDMATRIXINFO
