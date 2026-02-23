from ctypes import Structure, c_float

from ..base_classes import _S, BYTE


class struct_anon_65(Structure):
    pass

_S(struct_anon_65, [
    ('fVoltageValue', c_float),
    ('byVoltageAlarmType', BYTE),
    ('byRes1', BYTE * 3),
])

