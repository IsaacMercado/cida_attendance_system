from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_BV_SAMPLE_CALIB_POINT(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIB_POINT, [
    ('byCalibPtID', BYTE),
    ('byRes1', BYTE * 3),
    ('struPoint', NET_VCA_POINT),
    ('byRes2', BYTE * 16),
])

NET_DVR_BV_SAMPLE_CALIB_POINT = struct_tagNET_DVR_BV_SAMPLE_CALIB_POINT
LPET_DVR_BV_SAMPLE_CALIB_POINT = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIB_POINT)
tagNET_DVR_BV_SAMPLE_CALIB_POINT = struct_tagNET_DVR_BV_SAMPLE_CALIB_POINT
