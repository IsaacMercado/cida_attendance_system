from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byReserve', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwPlayMode', DWORD),
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
    ('sFileName', c_char * 128),
    ('byRes', BYTE * 64),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY_V41 = struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41 = POINTER(struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41)
tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41 = struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41
