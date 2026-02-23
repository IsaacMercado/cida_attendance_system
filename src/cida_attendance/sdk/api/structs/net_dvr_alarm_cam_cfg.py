from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarm_cam_info import NET_DVR_ALARM_CAM_INFO


class struct_tagNET_DVR_ALARM_CAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_CAM_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 7),
    ('dwNum', DWORD),
    ('struAlarmCam', NET_DVR_ALARM_CAM_INFO * 32),
])

NET_DVR_ALARM_CAM_CFG = struct_tagNET_DVR_ALARM_CAM_CFG
LPNET_DVR_ALARM_CAM_CFG = POINTER(struct_tagNET_DVR_ALARM_CAM_CFG)
tagNET_DVR_ALARM_CAM_CFG = struct_tagNET_DVR_ALARM_CAM_CFG
