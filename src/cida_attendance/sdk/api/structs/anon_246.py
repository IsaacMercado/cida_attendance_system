from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_246(Structure):
    pass

_S(struct_anon_246, [
    ('byRoomIndex', BYTE),
    ('byRes', BYTE * 799),
])

