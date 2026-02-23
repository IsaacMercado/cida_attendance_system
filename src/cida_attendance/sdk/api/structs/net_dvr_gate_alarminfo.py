from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_399 import union_anon_399
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_GATE_ALARMINFO(Structure):
    pass

_S(struct_tagNET_DVR_GATE_ALARMINFO, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byExternalDevType', BYTE),
    ('byExternalDevStatus', BYTE),
    ('byExternalDevCtrlType', BYTE),
    ('struAlarmTime', NET_DVR_TIME_V30),
    ('uAlarmInfo', union_anon_399),
    ('byRes2', BYTE * 64),
])

NET_DVR_GATE_ALARMINFO = struct_tagNET_DVR_GATE_ALARMINFO
LPNET_DVR_GATE_ALARMINFO = POINTER(struct_tagNET_DVR_GATE_ALARMINFO)
tagNET_DVR_GATE_ALARMINFO = struct_tagNET_DVR_GATE_ALARMINFO
