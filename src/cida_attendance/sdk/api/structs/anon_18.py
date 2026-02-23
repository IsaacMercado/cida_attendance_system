from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_anon_18(Structure):
    pass

_S(struct_anon_18, [
    ('byMotionScope', (BYTE * 96) * 64),
    ('byMotionSensitive', BYTE),
    ('byEnableHandleMotion', BYTE),
    ('byEnableDisplay', BYTE),
    ('reservedData', c_char),
    ('struMotionHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRelRecordChan', BYTE * int((32 + 32))),
])

NET_DVR_MOTION_V30 = struct_anon_18
LPNET_DVR_MOTION_V30 = POINTER(struct_anon_18)
