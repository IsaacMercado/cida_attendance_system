from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD


class struct_anon_269(Structure):
    pass

_S(struct_anon_269, [
    ('byRoomIndex', BYTE),
    ('byDriveIndex', BYTE),
    ('wSegmetSize', WORD),
    ('dwSegmentNo', DWORD),
    ('bySegmentState', BYTE),
    ('byCaseType', BYTE),
    ('byRes', BYTE * 2),
    ('byCaseNo', BYTE * 52),
    ('byCaseName', BYTE * 64),
    ('byLitigant1', BYTE * 24),
    ('byLitigant2', BYTE * 24),
    ('byChiefJudge', BYTE * 24),
    ('byRes1', BYTE * 104),
])

