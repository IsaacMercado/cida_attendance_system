from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_323(Structure):
    pass

_S(struct_anon_323, [
    ('dwSize', DWORD),
    ('dwEnabled', DWORD),
    ('sProtocalName', c_char * 16),
    ('byRes1', BYTE * 64),
    ('dwEnableSubStream', DWORD),
    ('byMainProType', BYTE),
    ('byMainTransType', BYTE),
    ('wMainPort', WORD),
    ('sMainPath', c_char * 256),
    ('bySubProType', BYTE),
    ('bySubTransType', BYTE),
    ('wSubPort', WORD),
    ('sSubPath', c_char * 256),
    ('byRes2', BYTE * 200),
])

NET_DVR_CUSTOM_PROTOCAL = struct_anon_323
LPNET_DVR_CUSTOM_PROTOCAL = POINTER(struct_anon_323)
