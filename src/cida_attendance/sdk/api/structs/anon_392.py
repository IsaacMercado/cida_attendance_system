from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_391 import NET_DVR_MOTION_MODE_PARAM


class struct_anon_392(Structure):
    pass

_S(struct_anon_392, [
    ('struMotionMode', NET_DVR_MOTION_MODE_PARAM),
    ('byEnableHandleMotion', BYTE),
    ('byEnableDisplay', BYTE),
    ('byConfigurationMode', BYTE),
    ('byKeyingEnable', BYTE),
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('dwMaxRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * 512),
    ('byDiscardFalseAlarm', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_MOTION_V40 = struct_anon_392
LPNET_DVR_MOTION_V40 = POINTER(struct_anon_392)
