from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_track_calibration_param import NET_DVR_TRACK_CALIBRATION_PARAM


class struct_tagNET_DVR_TRACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byFollowChan', BYTE),
    ('byDomeCalibrate', BYTE),
    ('byRes', BYTE),
    ('struCalParam', NET_DVR_TRACK_CALIBRATION_PARAM),
])

NET_DVR_TRACK_CFG = struct_tagNET_DVR_TRACK_CFG
LPNET_DVR_TRACK_CFG = POINTER(struct_tagNET_DVR_TRACK_CFG)
tagNET_DVR_TRACK_CFG = struct_tagNET_DVR_TRACK_CFG
