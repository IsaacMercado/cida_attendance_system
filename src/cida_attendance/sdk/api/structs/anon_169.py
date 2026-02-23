from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_169(Structure):
    pass

_S(struct_anon_169, [
    ('dwSize', DWORD),
    ('sDVRIP', c_char * 16),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byReserve', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwPlayMode', DWORD),
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
    ('sFileName', c_char * 128),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY = struct_anon_169
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY = POINTER(struct_anon_169)
