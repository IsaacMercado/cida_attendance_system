from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_120(Structure):
    pass

_S(struct_anon_120, [
    ('byEncoderIP', BYTE * 16),
    ('byEncoderUser', BYTE * 16),
    ('byEncoderPasswd', BYTE * 16),
    ('byEncoderChannel', BYTE),
    ('bySendMode', BYTE),
    ('wEncoderPort', WORD),
    ('dwConnectState', DWORD),
    ('reservedData', BYTE * 4),
])

NET_DVR_DECODERSTATE = struct_anon_120
LPNET_DVR_DECODERSTATE = POINTER(struct_anon_120)
