from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_ptz_info import NET_PTZ_INFO
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_CALIB_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CALIB_PARAM, [
    ('struPtzInfo', NET_PTZ_INFO),
    ('struCalibCoordinates', NET_VCA_POINT),
    ('iHorValue', c_int),
    ('iVerValue', c_int),
    ('byRes', BYTE * 8),
])

NET_DVR_CALIB_PARAM = struct_tagNET_DVR_CALIB_PARAM
LPNET_DVR_CALIB_PARAM = POINTER(struct_tagNET_DVR_CALIB_PARAM)
tagNET_DVR_CALIB_PARAM = struct_tagNET_DVR_CALIB_PARAM
