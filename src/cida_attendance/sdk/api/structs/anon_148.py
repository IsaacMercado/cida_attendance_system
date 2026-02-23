from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_148(Structure):
    pass

_S(struct_anon_148, [
    ('sNTPServer', BYTE * 64),
    ('wInterval', WORD),
    ('byEnableNTP', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('res1', BYTE),
    ('wNtpPort', WORD),
    ('res2', BYTE * 8),
])

NET_DVR_NTPPARA = struct_anon_148
LPNET_DVR_NTPPARA = POINTER(struct_anon_148)
