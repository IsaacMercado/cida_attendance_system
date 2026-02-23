from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM, [
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byRes', BYTE * 8),
])

NET_DVR_ALARMHOST_SEARCH_LOG_PARAM = struct_tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM
LPNET_DVR_ALARMHOST_SEARCH_LOG_PARAM = struct_tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM
tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM = struct_tagNET_DVR_ALARMHOST_SEARCH_LOG_PARAM
