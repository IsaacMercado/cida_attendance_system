from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_search_cond import NET_DVR_TIME_SEARCH_COND


class struct_tagNET_DVR_ALARM_SEARCH_COND(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_SEARCH_COND, [
    ('dwSize', DWORD),
    ('strStartTime', NET_DVR_TIME_SEARCH_COND),
    ('strStopTime', NET_DVR_TIME_SEARCH_COND),
    ('dwAlarmComm', DWORD),
    ('sAlarmUID', c_char * 64),
    ('wEventType', WORD),
    ('wSubEventType', WORD),
    ('bySupport', BYTE),
    ('byNoBoundary', BYTE),
    ('byRes', BYTE * 122),
])

NET_DVR_ALARM_SEARCH_COND = struct_tagNET_DVR_ALARM_SEARCH_COND
LPNET_DVR_ALARM_SEARCH_COND = POINTER(struct_tagNET_DVR_ALARM_SEARCH_COND)
tagNET_DVR_ALARM_SEARCH_COND = struct_tagNET_DVR_ALARM_SEARCH_COND
