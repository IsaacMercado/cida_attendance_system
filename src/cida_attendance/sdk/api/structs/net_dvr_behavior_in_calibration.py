from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_camera_param import NET_DVR_CAMERA_PARAM
from .net_dvr_in_cal_sample import NET_DVR_IN_CAL_SAMPLE


class struct_tagNET_DVR_BEHAVIOR_IN_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_BEHAVIOR_IN_CALIBRATION, [
    ('dwCalSampleNum', DWORD),
    ('struCalSample', NET_DVR_IN_CAL_SAMPLE * 5),
    ('struCameraParam', NET_DVR_CAMERA_PARAM),
    ('byRes', BYTE * 16),
])

NET_DVR_BEHAVIOR_IN_CALIBRATION = struct_tagNET_DVR_BEHAVIOR_IN_CALIBRATION
LPNET_DVR_BEHAVIOR_IN_CALIBRATION = POINTER(struct_tagNET_DVR_BEHAVIOR_IN_CALIBRATION)
tagNET_DVR_BEHAVIOR_IN_CALIBRATION = struct_tagNET_DVR_BEHAVIOR_IN_CALIBRATION
