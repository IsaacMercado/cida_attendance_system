from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SWITCH_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_ALARM, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('wSwitchChannel', WORD),
    ('byAlarmType', BYTE),
    ('byRes', BYTE * 41),
])

NET_DVR_SWITCH_ALARM = struct_tagNET_DVR_SWITCH_ALARM
LPNET_DVR_SWITCH_ALARM = POINTER(struct_tagNET_DVR_SWITCH_ALARM)
tagNET_DVR_SWITCH_ALARM = struct_tagNET_DVR_SWITCH_ALARM
