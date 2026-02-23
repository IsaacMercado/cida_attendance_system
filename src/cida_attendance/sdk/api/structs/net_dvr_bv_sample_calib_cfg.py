from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_bv_sample_calib_point import NET_DVR_BV_SAMPLE_CALIB_POINT


class struct_tagNET_DVR_BV_SAMPLE_CALIB_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIB_CFG, [
    ('dwSize', DWORD),
    ('dwCameraHeight', DWORD),
    ('fPitchAngle', c_float),
    ('fInclineAngle', c_float),
    ('struCalibPoint', NET_DVR_BV_SAMPLE_CALIB_POINT * 5),
    ('struCalibPointEx', NET_DVR_BV_SAMPLE_CALIB_POINT * 7),
    ('byRes', BYTE * 60),
])

NET_DVR_BV_SAMPLE_CALIB_CFG = struct_tagNET_DVR_BV_SAMPLE_CALIB_CFG
LPNET_DVR_BV_SAMPLE_CALIB_CFG = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIB_CFG)
tagNET_DVR_BV_SAMPLE_CALIB_CFG = struct_tagNET_DVR_BV_SAMPLE_CALIB_CFG
