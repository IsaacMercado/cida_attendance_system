from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_268(Structure):
    pass

_S(struct_anon_268, [
    ('dwRecordType', DWORD),
    ('dwRecordLength', DWORD),
    ('byLockFlag', BYTE),
    ('byDrawFrameType', BYTE),
    ('byRes1', BYTE * 2),
    ('byFileName', BYTE * 32),
    ('dwFileIndex', DWORD),
    ('byRes', BYTE * 256),
])

