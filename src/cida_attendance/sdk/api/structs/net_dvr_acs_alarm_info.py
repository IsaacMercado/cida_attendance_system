from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_acs_event_info import NET_DVR_ACS_EVENT_INFO


class struct_tagNET_DVR_ACS_ALARM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACS_ALARM_INFO, [
    ('dwSize', DWORD),
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('struTime', NET_DVR_TIME),
    ('sNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('struAcsEventInfo', NET_DVR_ACS_EVENT_INFO),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('wInductiveEventType', WORD),
    ('byPicTransType', BYTE),
    ('byRes1', BYTE),
    ('dwIOTChannelNo', DWORD),
    ('pAcsEventInfoExtend', String),
    ('byAcsEventInfoExtend', BYTE),
    ('byTimeType', BYTE),
    ('byRes2', BYTE),
    ('byAcsEventInfoExtendV20', BYTE),
    ('pAcsEventInfoExtendV20', String),
    ('byRes', BYTE * 4),
])

NET_DVR_ACS_ALARM_INFO = struct_tagNET_DVR_ACS_ALARM_INFO
LPNET_DVR_ACS_ALARM_INFO = POINTER(struct_tagNET_DVR_ACS_ALARM_INFO)
tagNET_DVR_ACS_ALARM_INFO = struct_tagNET_DVR_ACS_ALARM_INFO
