from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_lock_alarm_info import NET_DVR_LOCK_ALARM_INFO
from .net_dvr_zone_alarm_info import NET_DVR_ZONE_ALARM_INFO


class union_tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION(Union):
    pass

_S(union_tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION, [
    ('byLen', BYTE * 256),
    ('struZoneAlarm', NET_DVR_ZONE_ALARM_INFO),
    ('struLockAlarm', NET_DVR_LOCK_ALARM_INFO),
])

NET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION = union_tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION
LPNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION = POINTER(union_tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION)
tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION = union_tagNET_DVR_VIDEO_INTERCOM_ALARM_INFO_UNION
