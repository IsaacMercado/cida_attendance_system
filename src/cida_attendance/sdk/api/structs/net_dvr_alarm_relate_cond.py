from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_RELATE_COND(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_RELATE_COND, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byRelateActType', BYTE),
    ('byRes', BYTE * 2),
    ('dwChannel', DWORD),
    ('byRes1', BYTE * 64),
])

NET_DVR_ALARM_RELATE_COND = struct_tagNET_DVR_ALARM_RELATE_COND
LPNET_DVR_ALARM_RELATE_COND = POINTER(struct_tagNET_DVR_ALARM_RELATE_COND)
tagNET_DVR_ALARM_RELATE_COND = struct_tagNET_DVR_ALARM_RELATE_COND
