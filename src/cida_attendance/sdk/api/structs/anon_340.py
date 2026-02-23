from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_340(Structure):
    pass

_S(struct_anon_340, [
    ('byIONo', BYTE),
    ('byTriggerType', BYTE),
    ('byRes1', BYTE * 2),
])

