from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_50(Structure):
    pass

_S(struct_anon_50, [
    ('sRemoteIP', c_char * 16),
    ('sLocalIP', c_char * 16),
    ('sLocalIPMask', c_char * 16),
    ('sUsername', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byPPPMode', BYTE),
    ('byRedial', BYTE),
    ('byRedialMode', BYTE),
    ('byDataEncrypt', BYTE),
    ('dwMTU', DWORD),
    ('sTelephoneNumber', c_char * 32),
])

NET_DVR_PPPCFG = struct_anon_50
LPNET_DVR_PPPCFG = POINTER(struct_anon_50)
