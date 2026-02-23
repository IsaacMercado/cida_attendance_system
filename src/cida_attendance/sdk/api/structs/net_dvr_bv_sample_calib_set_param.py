from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_bv_sample_calib_point import NET_DVR_BV_SAMPLE_CALIB_POINT


class struct_tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM, [
    ('struCalibPoint', NET_DVR_BV_SAMPLE_CALIB_POINT),
    ('byRes', BYTE * 228),
])

NET_DVR_BV_SAMPLE_CALIB_SET_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM
LPNET_DVR_BV_SAMPLE_CALIB_SET_PARAM = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM)
tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_SET_PARAM
