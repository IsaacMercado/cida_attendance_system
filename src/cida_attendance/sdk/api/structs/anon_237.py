from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_237(Structure):
    pass

_S(struct_anon_237, [
    ('byRoomIndex', BYTE),
    ('byRes1', BYTE * 3),
    ('sInquestInfo', BYTE * 64),
    ('byRes2', BYTE * 232),
])

