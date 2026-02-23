from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_camera_param import NET_DVR_CAMERA_PARAM
from .net_dvr_line_segment import NET_DVR_LINE_SEGMENT


class struct_tagNET_DVR_BEHAVIOR_OUT_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_BEHAVIOR_OUT_CALIBRATION, [
    ('dwLineSegNum', DWORD),
    ('struLineSegment', NET_DVR_LINE_SEGMENT * 8),
    ('struCameraParam', NET_DVR_CAMERA_PARAM),
    ('byRes', BYTE * 20),
])

NET_DVR_BEHAVIOR_OUT_CALIBRATION = struct_tagNET_DVR_BEHAVIOR_OUT_CALIBRATION
LPNET_DVR_BEHAVIOR_OUT_CALIBRATION = POINTER(struct_tagNET_DVR_BEHAVIOR_OUT_CALIBRATION)
tagNET_DVR_BEHAVIOR_OUT_CALIBRATION = struct_tagNET_DVR_BEHAVIOR_OUT_CALIBRATION
