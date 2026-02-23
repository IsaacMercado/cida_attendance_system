from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ptz_ctrl import NET_DVR_PTZ_CTRL


class struct_tagNET_DVR_ALARM_CAM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_CAM_INFO, [
    ('dwCamID', DWORD),
    ('dwRecordTime', DWORD),
    ('dwMonID', DWORD),
    ('dwResidentTime', DWORD),
    ('struPtzCtrl', NET_DVR_PTZ_CTRL),
    ('byAlarmOffMode', BYTE),
    ('byDevType', BYTE),
    ('byDecChan', BYTE),
    ('byRes', BYTE * 17),
])

NET_DVR_ALARM_CAM_INFO = struct_tagNET_DVR_ALARM_CAM_INFO
LPNET_DVR_ALARM_CAM_INFO = POINTER(struct_tagNET_DVR_ALARM_CAM_INFO)
tagNET_DVR_ALARM_CAM_INFO = struct_tagNET_DVR_ALARM_CAM_INFO
