from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_275(Structure):
    pass

_S(struct_anon_275, [
    ('dwRecordType', DWORD),
    ('dwRecordLength', DWORD),
    ('byLockFlag', BYTE),
    ('byDrawFrameType', BYTE),
    ('byPosition', BYTE),
    ('byRes1', BYTE),
    ('byFileName', BYTE * 32),
    ('dwFileIndex', DWORD),
    ('byTapeIndex', BYTE * 32),
    ('byFileNameEx', BYTE * 256),
    ('byRes', BYTE * 464),
])

