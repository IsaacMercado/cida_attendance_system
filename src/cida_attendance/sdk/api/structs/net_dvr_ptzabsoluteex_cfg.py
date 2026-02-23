from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_ptz_info import NET_PTZ_INFO


class struct_tagNET_DVR_PTZABSOLUTEEX_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZABSOLUTEEX_CFG, [
    ('dwSize', DWORD),
    ('struPTZCtrl', NET_PTZ_INFO),
    ('dwFocalLen', DWORD),
    ('fHorizontalSpeed', c_float),
    ('fVerticalSpeed', c_float),
    ('byZoomType', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_PTZABSOLUTEEX_CFG = struct_tagNET_DVR_PTZABSOLUTEEX_CFG
LPNET_DVR_PTZABSOLUTEEX_CFG = POINTER(struct_tagNET_DVR_PTZABSOLUTEEX_CFG)
tagNET_DVR_PTZABSOLUTEEX_CFG = struct_tagNET_DVR_PTZABSOLUTEEX_CFG
