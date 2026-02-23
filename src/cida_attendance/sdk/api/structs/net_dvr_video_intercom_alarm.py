from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_dvr_video_intercom_alarm_info_union import (
    NET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION,
)


class struct_tagNET_DVR_VIDEO_INTERCOM_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_ALARM, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_EX),
    ('byDevNumber', BYTE * 32),
    ('byAlarmType', BYTE),
    ('byRes1', BYTE * 3),
    ('uAlarmInfo', NET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION),
    ('wLockID', WORD),
    ('byRes3', BYTE * 2),
    ('dwIOTChannelNo', DWORD),
    ('byRes2', BYTE * 248),
])

NET_DVR_VIDEO_INTERCOM_ALARM = struct_tagNET_DVR_VIDEO_INTERCOM_ALARM
LPNET_DVR_VIDEO_INTERCOM_ALARM = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_ALARM)
tagNET_DVR_VIDEO_INTERCOM_ALARM = struct_tagNET_DVR_VIDEO_INTERCOM_ALARM
