from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_256(Structure):
    pass

_S(struct_anon_256, [
    ('byRoomIndex', BYTE),
    ('byRes', BYTE * 799),
])

