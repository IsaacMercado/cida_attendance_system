from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_485_device_alarm_union import NET_DVR_485_DEVICE_ALARM_UNION


class struct_tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO(Structure):
    pass

_S(struct_tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmInfo', NET_DVR_485_DEVICE_ALARM_UNION),
    ('byRes2', BYTE * 16),
])

NET_DVR_485_EXTERNAL_DEVICE_ALARMINFO = struct_tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO
LPNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO = POINTER(struct_tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO)
tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO = struct_tagNET_DVR_485_EXTERNAL_DEVICE_ALARMINFO
