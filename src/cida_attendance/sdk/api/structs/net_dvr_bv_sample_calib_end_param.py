from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM, [
    ('byRes', BYTE * 256),
])

NET_DVR_BV_SAMPLE_CALIB_END_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM
LPNET_DVR_BV_SAMPLE_CALIB_END_PARAM = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM)
tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_END_PARAM
