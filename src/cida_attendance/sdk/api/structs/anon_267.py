from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD


class struct_anon_267(Structure):
    pass

_S(struct_anon_267, [
    ('byRoomIndex', BYTE),
    ('byDriveIndex', BYTE),
    ('byRes1', BYTE * 6),
    ('dwSegmentNo', DWORD),
    ('wSegmetSize', WORD),
    ('wSegmentState', WORD),
    ('byRes2', BYTE * 288),
])

