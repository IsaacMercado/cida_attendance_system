from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_llpos_param import NET_DVR_LLPOS_PARAM
from .net_ptz_info import NET_PTZ_INFO
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_SMOKEDETECTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SMOKEDETECTION_ALARM, [
    ('struPTZPos', NET_PTZ_INFO),
    ('struThermalPTZPos', NET_PTZ_INFO),
    ('struLLPos', NET_DVR_LLPOS_PARAM),
    ('struSmokePos', NET_VCA_RECT),
    ('byRes', BYTE * 256),
])

NET_DVR_SMOKEDETECTION_ALARM = struct_tagNET_DVR_SMOKEDETECTION_ALARM
LPNET_DVR_SMOKEDETECTION_ALARM = POINTER(struct_tagNET_DVR_SMOKEDETECTION_ALARM)
tagNET_DVR_SMOKEDETECTION_ALARM = struct_tagNET_DVR_SMOKEDETECTION_ALARM
