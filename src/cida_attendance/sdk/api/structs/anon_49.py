from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_49(Structure):
    pass

_S(struct_anon_49, [
    ('struRemoteIP', NET_DVR_IPADDR),
    ('struLocalIP', NET_DVR_IPADDR),
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

NET_DVR_PPPCFG_V30 = struct_anon_49
LPNET_DVR_PPPCFG_V30 = POINTER(struct_anon_49)
