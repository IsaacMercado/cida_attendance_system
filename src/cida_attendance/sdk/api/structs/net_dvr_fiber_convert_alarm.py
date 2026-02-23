from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FIBER_CONVERT_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_ALARM, [
    ('dwSize', DWORD),
    ('dwEventType', DWORD),
    ('dwEvent', DWORD),
    ('bySlotNum', BYTE),
    ('byCardType', BYTE),
    ('byPortNo', BYTE),
    ('byCurTemperature', BYTE),
    ('wCurVoltage', WORD),
    ('byRes1', BYTE * 30),
])

NET_DVR_FIBER_CONVERT_ALARM = struct_tagNET_DVR_FIBER_CONVERT_ALARM
LPNET_DVR_FIBER_CONVERT_ALARM = POINTER(struct_tagNET_DVR_FIBER_CONVERT_ALARM)
tagNET_DVR_FIBER_CONVERT_ALARM = struct_tagNET_DVR_FIBER_CONVERT_ALARM
