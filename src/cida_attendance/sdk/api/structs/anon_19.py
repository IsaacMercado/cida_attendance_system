from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_8 import NET_DVR_HANDLEEXCEPTION


class struct_anon_19(Structure):
    pass

_S(struct_anon_19, [
    ('byMotionScope', (BYTE * 22) * 18),
    ('byMotionSensitive', BYTE),
    ('byEnableHandleMotion', BYTE),
    ('byEnableDisplay', BYTE),
    ('reservedData', c_char),
    ('strMotionHandleType', NET_DVR_HANDLEEXCEPTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
    ('byRelRecordChan', BYTE * 16),
])

NET_DVR_MOTION = struct_anon_19
LPNET_DVR_MOTION = POINTER(struct_anon_19)
