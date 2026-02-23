from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_bv_sample_calib_begin_param import NET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM
from .net_dvr_bv_sample_calib_end_param import NET_DVR_BV_SAMPLE_CALIB_END_PARAM
from .net_dvr_bv_sample_calib_set_param import NET_DVR_BV_SAMPLE_CALIB_SET_PARAM


class union_tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION, [
    ('byRes', BYTE * 256),
    ('struCalibBegin', NET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM),
    ('struCalibSet', NET_DVR_BV_SAMPLE_CALIB_SET_PARAM),
    ('struCalibEnd', NET_DVR_BV_SAMPLE_CALIB_END_PARAM),
])

NET_DVR_BV_SAMPLE_CALIB_PARAM_UNION = union_tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION
LPNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION = POINTER(union_tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION)
tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION = union_tagNET_DVR_BV_SAMPLE_CALIB_PARAM_UNION
