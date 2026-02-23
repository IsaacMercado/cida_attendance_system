from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_BV_CALIB_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_PARAM, [
    ('dwPicID', DWORD),
    ('struPoint', NET_VCA_POINT),
    ('byRes', BYTE * 32),
])

NET_DVR_BV_CALIB_PARAM = struct_tagNET_DVR_BV_CALIB_PARAM
LPNET_DVR_BV_CALIB_PARAM = POINTER(struct_tagNET_DVR_BV_CALIB_PARAM)
tagNET_DVR_BV_CALIB_PARAM = struct_tagNET_DVR_BV_CALIB_PARAM
