from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_250(Structure):
    pass

_S(struct_anon_250, [
    ('byCaseNo', BYTE * 56),
    ('byCaseName', BYTE * 100),
    ('byLitigant1', BYTE * 32),
    ('byLitigant2', BYTE * 32),
    ('byChiefJudge', BYTE * 32),
    ('byCaseType', BYTE),
    ('byRes', BYTE * 47),
])

