from ctypes import Structure, c_char

from ..base_classes import _S, BYTE


class struct_anon_398(Structure):
    pass

_S(struct_anon_398, [
    ('sLicense', c_char * 16),
    ('byVehicleType', BYTE),
    ('byRes1', BYTE * 111),
])

