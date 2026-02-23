from ctypes import Structure

from ..base_classes import _S, DWORD


class struct_anon_61(Structure):
    pass

_S(struct_anon_61, [
    ('dwAlarmInputNo', DWORD),
    ('dwTrigerAlarmOutNum', DWORD),
    ('dwTrigerRecordChanNum', DWORD),
])

