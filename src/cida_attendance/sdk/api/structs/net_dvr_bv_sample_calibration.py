from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_bv_sample_calib_param_union import NET_DVR_BV_SAMPLE_CALIB_PARAM_UNION


class struct_tagNET_DVR_BV_SAMPLE_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIBRATION, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byCommand', BYTE),
    ('byRes1', BYTE * 3),
    ('uCalibParam', NET_DVR_BV_SAMPLE_CALIB_PARAM_UNION),
    ('byRes2', BYTE * 256),
])

NET_DVR_BV_SAMPLE_CALIBRATION = struct_tagNET_DVR_BV_SAMPLE_CALIBRATION
LPNET_DVR_BV_SAMPLE_CALIBRATION = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIBRATION)
tagNET_DVR_BV_SAMPLE_CALIBRATION = struct_tagNET_DVR_BV_SAMPLE_CALIBRATION
