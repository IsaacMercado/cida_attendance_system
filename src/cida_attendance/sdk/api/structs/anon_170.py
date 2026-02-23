from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_170(Structure):
    pass

_S(struct_anon_170, [
    ('dwSize', DWORD),
    ('dwPlayCmd', DWORD),
    ('dwCmdParam', DWORD),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY_CONTROL = struct_anon_170
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_CONTROL = POINTER(struct_anon_170)
