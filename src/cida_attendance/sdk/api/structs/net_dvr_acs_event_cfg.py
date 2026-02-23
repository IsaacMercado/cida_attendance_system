from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_acs_event_detail import NET_DVR_ACS_EVENT_DETAIL


class struct_tagNET_DVR_ACS_EVENT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_CFG, [
    ('dwSize', DWORD),
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('struTime', NET_DVR_TIME),
    ('sNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('struAcsEventInfo', NET_DVR_ACS_EVENT_DETAIL),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('wInductiveEventType', WORD),
    ('byTimeType', BYTE),
    ('byRes1', BYTE),
    ('dwQRCodeInfoLen', DWORD),
    ('dwVisibleLightDataLen', DWORD),
    ('dwThermalDataLen', DWORD),
    ('pQRCodeInfo', String),
    ('pVisibleLightData', String),
    ('pThermalData', String),
    ('byRes', BYTE * 36),
])

NET_DVR_ACS_EVENT_CFG = struct_tagNET_DVR_ACS_EVENT_CFG
LPNET_DVR_ACS_EVENT_CFG = POINTER(struct_tagNET_DVR_ACS_EVENT_CFG)
tagNET_DVR_ACS_EVENT_CFG = struct_tagNET_DVR_ACS_EVENT_CFG
