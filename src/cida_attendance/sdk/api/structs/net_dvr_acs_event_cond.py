from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_ACS_EVENT_COND(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_COND, [
    ('dwSize', DWORD),
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byCardNo', BYTE * 32),
    ('byName', BYTE * 32),
    ('byPicEnable', BYTE),
    ('byTimeType', BYTE),
    ('byRes2', BYTE * 2),
    ('dwBeginSerialNo', DWORD),
    ('dwEndSerialNo', DWORD),
    ('dwIOTChannelNo', DWORD),
    ('wInductiveEventType', WORD),
    ('bySearchType', BYTE),
    ('byEventAttribute', BYTE),
    ('szMonitorID', c_char * 64),
    ('byEmployeeNo', BYTE * 32),
    ('byRes', BYTE * 140),
])

NET_DVR_ACS_EVENT_COND = struct_tagNET_DVR_ACS_EVENT_COND
LPNET_DVR_ACS_EVENT_COND = POINTER(struct_tagNET_DVR_ACS_EVENT_COND)
tagNET_DVR_ACS_EVENT_COND = struct_tagNET_DVR_ACS_EVENT_COND
