from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_160(Structure):
    pass

_S(struct_anon_160, [
    ('sDVRIP', c_char * 16),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byRes', BYTE * 3),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
])

NET_DVR_MATRIX_DECINFO = struct_anon_160
LPNET_DVR_MATRIX_DECINFO = POINTER(struct_anon_160)
