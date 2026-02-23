from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_186 import NET_DVR_PTZPOS
from .net_dvr_cb_point import NET_DVR_CB_POINT


class struct_tagNET_DVR_TRACK_CALIBRATION_PARAM_V41(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_CALIBRATION_PARAM_V41, [
    ('byPointNum', BYTE),
    ('byRes', BYTE * 3),
    ('struCBPoint', NET_DVR_CB_POINT * 6),
    ('struHorizonPtzPos', NET_DVR_PTZPOS),
    ('byRes2', BYTE * 256),
])

NET_DVR_TRACK_CALIBRATION_PARAM_V41 = struct_tagNET_DVR_TRACK_CALIBRATION_PARAM_V41
LPNET_DVR_TRACK_CALIBRATION_PARAM_V41 = POINTER(struct_tagNET_DVR_TRACK_CALIBRATION_PARAM_V41)
tagNET_DVR_TRACK_CALIBRATION_PARAM_V41 = struct_tagNET_DVR_TRACK_CALIBRATION_PARAM_V41
