from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD


class struct_anon_262(Structure):
    pass

_S(struct_anon_262, [
    ('wDeviceType', WORD),
    ('wEventType', WORD),
    ('wChannel', WORD * int((32 + 32))),
    ('byAllChan', BYTE),
    ('byCaseSensitive', BYTE),
    ('byCombinateMode', BYTE),
    ('bySearchType', BYTE),
    ('sKeyWord', (c_char * 128) * 3),
    ('wZoneNo', WORD),
    ('byRes', BYTE * 278),
])

