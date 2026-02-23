from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_172 import union_anon_172
from .anon_173 import union_anon_173


class struct_tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX(Structure):
    pass

_S(struct_tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX, [
    ('dwSize', DWORD),
    ('dwDecChannel', DWORD),
    ('byAddressType', BYTE),
    ('byChannelType', BYTE),
    ('byres', BYTE * 2),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwChannel', DWORD),
    ('byStreamId', BYTE * 32),
    ('dwPlayMode', DWORD),
    ('unionAddr', union_anon_172),
    ('unionPlayBackInfo', union_anon_173),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY_EX = struct_tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_EX = POINTER(struct_tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX)
tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX = struct_tagNet_DVR_MATRIX_DEC_REMOTE_PLAY_EX
