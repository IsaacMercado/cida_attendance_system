from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_119(Structure):
    pass

_S(struct_anon_119, [
    ('byEncoderIP', BYTE * 16),
    ('byEncoderUser', BYTE * 16),
    ('byEncoderPasswd', BYTE * 16),
    ('bySendMode', BYTE),
    ('byEncoderChannel', BYTE),
    ('wEncoderPort', WORD),
    ('reservedData', BYTE * 4),
])

NET_DVR_DECODERINFO = struct_anon_119
LPNET_DVR_DECODERINFO = POINTER(struct_anon_119)
