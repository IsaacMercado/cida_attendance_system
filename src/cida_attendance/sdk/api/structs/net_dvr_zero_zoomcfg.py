from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_ZERO_ZOOMCFG(Structure):
    pass

_S(struct_tagNET_DVR_ZERO_ZOOMCFG, [
    ('dwSize', DWORD),
    ('struPoint', NET_VCA_POINT),
    ('byState', BYTE),
    ('byPreviewNumber', BYTE),
    ('byPreviewSeq', BYTE * 32),
    ('byRes', BYTE * 30),
])

NET_DVR_ZERO_ZOOMCFG = struct_tagNET_DVR_ZERO_ZOOMCFG
LPNET_DVR_ZERO_ZOOMCFG = POINTER(struct_tagNET_DVR_ZERO_ZOOMCFG)
tagNET_DVR_ZERO_ZOOMCFG = struct_tagNET_DVR_ZERO_ZOOMCFG
