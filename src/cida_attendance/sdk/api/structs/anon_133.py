from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_132 import union_anon_132


class struct_anon_133(Structure):
    pass

_S(struct_anon_133, [
    ('dwWorkType', DWORD),
    ('sDVRIP', c_char * 16),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byLinkMode', BYTE),
    ('dwLinkType', DWORD),
    ('objectInfo', union_anon_132),
])

NET_DVR_DECCHANSTATUS = struct_anon_133
LPNET_DVR_DECCHANSTATUS = POINTER(struct_anon_133)
