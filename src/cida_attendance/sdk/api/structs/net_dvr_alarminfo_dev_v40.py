from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_alarm_cvr_subinfo_union import NET_ALARM_CVR_SUBINFO_UNION


class struct_tagNET_DVR_ALARMINFO_DEV_V40(Structure):
    pass

_S(struct_tagNET_DVR_ALARMINFO_DEV_V40, [
    ('dwAlarmType', DWORD),
    ('struTime', NET_DVR_TIME),
    ('uSubAlarmInfo', NET_ALARM_CVR_SUBINFO_UNION),
    ('byRes', BYTE * 256),
    ('dwNumber', DWORD),
    ('pNO', POINTER(WORD)),
])

NET_DVR_ALARMINFO_DEV_V40 = struct_tagNET_DVR_ALARMINFO_DEV_V40
LPNET_DVR_ALARMINFO_DEV_V40 = POINTER(struct_tagNET_DVR_ALARMINFO_DEV_V40)
tagNET_DVR_ALARMINFO_DEV_V40 = struct_tagNET_DVR_ALARMINFO_DEV_V40
