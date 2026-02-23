from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_121(Structure):
    pass

_S(struct_anon_121, [
    ('sDVRIP', c_char * 16),
    ('wDVRPort', WORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byChannel', BYTE),
    ('byLinkMode', BYTE),
    ('byLinkType', BYTE),
])

NET_DVR_DECCHANINFO = struct_anon_121
LPNET_DVR_DECCHANINFO = POINTER(struct_anon_121)
