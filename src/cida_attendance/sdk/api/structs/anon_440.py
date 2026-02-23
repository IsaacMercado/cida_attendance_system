from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_440(Structure):
    pass

_S(struct_anon_440, [
    ('dwSize', DWORD),
    ('wPort', WORD),
    ('byPortState', BYTE),
    ('byRes', BYTE * 61),
])

NET_DVR_T1TEST_PARAMCFG = struct_anon_440
LPNET_DVR_T1TEST_PARAMCFG = POINTER(struct_anon_440)
