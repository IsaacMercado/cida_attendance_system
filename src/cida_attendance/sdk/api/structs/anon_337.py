from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_337(Structure):
    pass

_S(struct_anon_337, [
    ('byIONo', BYTE),
    ('byTriggerType', BYTE),
    ('byRes1', BYTE * 2),
])

