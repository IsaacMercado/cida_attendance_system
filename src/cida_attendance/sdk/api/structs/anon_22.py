from ctypes import Structure

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_8 import NET_DVR_HANDLEEXCEPTION


class struct_anon_22(Structure):
    pass

_S(struct_anon_22, [
    ('dwEnableHideAlarm', DWORD),
    ('wHideAlarmAreaTopLeftX', WORD),
    ('wHideAlarmAreaTopLeftY', WORD),
    ('wHideAlarmAreaWidth', WORD),
    ('wHideAlarmAreaHeight', WORD),
    ('strHideAlarmHandleType', NET_DVR_HANDLEEXCEPTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
])

NET_DVR_HIDEALARM = struct_anon_22
LPNET_DVR_HIDEALARM = POINTER(struct_anon_22)
