from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_call_info import NET_DVR_CALL_INFO


class struct_tagNET_DVR_CONFERENCE_CALL_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_CONFERENCE_CALL_ALARM, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byCallType', BYTE),
    ('byAutoAnswer', BYTE),
    ('byCallStatusSwitch', BYTE),
    ('struCallInfo', NET_DVR_CALL_INFO),
    ('byRes2', BYTE * 32),
])

NET_DVR_CONFERENCE_CALL_ALARM = struct_tagNET_DVR_CONFERENCE_CALL_ALARM
LPNET_DVR_CONFERENCE_CALL_ALARM = POINTER(struct_tagNET_DVR_CONFERENCE_CALL_ALARM)
tagNET_DVR_CONFERENCE_CALL_ALARM = struct_tagNET_DVR_CONFERENCE_CALL_ALARM
