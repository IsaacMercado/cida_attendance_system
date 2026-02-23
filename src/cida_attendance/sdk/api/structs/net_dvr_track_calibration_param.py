from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_cb_point import NET_DVR_CB_POINT


class struct_tagNET_DVR_TRACK_CALIBRATION_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_CALIBRATION_PARAM, [
    ('byPointNum', BYTE),
    ('byRes', BYTE * 3),
    ('struCBPoint', NET_DVR_CB_POINT * 6),
])

NET_DVR_TRACK_CALIBRATION_PARAM = struct_tagNET_DVR_TRACK_CALIBRATION_PARAM
LPNET_DVR_TRACK_CALIBRATION_PARAM = POINTER(struct_tagNET_DVR_TRACK_CALIBRATION_PARAM)
tagNET_DVR_TRACK_CALIBRATION_PARAM = struct_tagNET_DVR_TRACK_CALIBRATION_PARAM
