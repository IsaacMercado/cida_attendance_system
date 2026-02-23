from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_20(Structure):
    pass

_S(struct_anon_20, [
    ('dwEnableHideAlarm', DWORD),
    ('wHideAlarmAreaTopLeftX', WORD),
    ('wHideAlarmAreaTopLeftY', WORD),
    ('wHideAlarmAreaWidth', WORD),
    ('wHideAlarmAreaHeight', WORD),
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes', BYTE * 64),
])

NET_DVR_HIDEALARM_V40 = struct_anon_20
LPNET_DVR_HIDEALARM_V40 = POINTER(struct_anon_20)
