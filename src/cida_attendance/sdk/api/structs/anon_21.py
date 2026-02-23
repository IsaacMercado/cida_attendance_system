from ctypes import Structure

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_anon_21(Structure):
    pass

_S(struct_anon_21, [
    ('dwEnableHideAlarm', DWORD),
    ('wHideAlarmAreaTopLeftX', WORD),
    ('wHideAlarmAreaTopLeftY', WORD),
    ('wHideAlarmAreaWidth', WORD),
    ('wHideAlarmAreaHeight', WORD),
    ('strHideAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
])

NET_DVR_HIDEALARM_V30 = struct_anon_21
LPNET_DVR_HIDEALARM_V30 = POINTER(struct_anon_21)
