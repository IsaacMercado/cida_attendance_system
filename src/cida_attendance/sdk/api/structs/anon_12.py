from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_12(Structure):
    pass

_S(struct_anon_12, [
    ('dwPPPOE', DWORD),
    ('sPPPoEUser', BYTE * 32),
    ('sPPPoEPassword', c_char * 16),
    ('struPPPoEIP', NET_DVR_IPADDR),
])

NET_DVR_PPPOECFG = struct_anon_12
LPNET_DVR_PPPOECFG = POINTER(struct_anon_12)
