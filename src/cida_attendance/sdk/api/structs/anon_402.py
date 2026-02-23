from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_402(Structure):
    pass

_S(struct_anon_402, [
    ('iWaterLogVal', c_int),
    ('iLeakResist1', c_int),
    ('iTotolResist1', c_int),
    ('iLeakResist2', c_int),
    ('iTotolResist2', c_int),
    ('byWaterLogAlarm', BYTE),
    ('byLeakAlarm1', BYTE),
    ('byFaultAlarm1', BYTE),
    ('byLeakAlarm2', BYTE),
    ('byFaultAlarm2', BYTE),
    ('byRes', BYTE * 487),
])

NET_DVR_SOAK_STATE = struct_anon_402
LPNET_DVR_SOAK_STATE = POINTER(struct_anon_402)
