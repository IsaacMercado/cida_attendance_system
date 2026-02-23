from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_matrixcodesysteminfo import NET_DVR_MATRIXCODESYSTEMINFO
from .net_dvr_matrixdecodesysteminfo import NET_DVR_MATRIXDECODESYSTEMINFO


class struct_tagNET_DVR_MATRIXSWITCH(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXSWITCH, [
    ('struInputNote', NET_DVR_MATRIXCODESYSTEMINFO),
    ('struOutputNote', NET_DVR_MATRIXDECODESYSTEMINFO),
    ('byRes', BYTE * 32),
])

NET_DVR_MATRIXSWITCH = struct_tagNET_DVR_MATRIXSWITCH
LPNET_DVR_MATRIXSWITCH = POINTER(struct_tagNET_DVR_MATRIXSWITCH)
tagNET_DVR_MATRIXSWITCH = struct_tagNET_DVR_MATRIXSWITCH
