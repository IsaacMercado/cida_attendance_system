from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_11 import NET_DVR_ETHERNET


class struct_anon_16(Structure):
    pass

_S(struct_anon_16, [
    ('dwSize', DWORD),
    ('struEtherNet', NET_DVR_ETHERNET * 2),
    ('sManageHostIP', c_char * 16),
    ('wManageHostPort', WORD),
    ('sIPServerIP', c_char * 16),
    ('sMultiCastIP', c_char * 16),
    ('sGatewayIP', c_char * 16),
    ('sNFSIP', c_char * 16),
    ('sNFSDirectory', BYTE * 128),
    ('dwPPPOE', DWORD),
    ('sPPPoEUser', BYTE * 32),
    ('sPPPoEPassword', c_char * 16),
    ('sPPPoEIP', c_char * 16),
    ('wHttpPort', WORD),
])

NET_DVR_NETCFG = struct_anon_16
LPNET_DVR_NETCFG = POINTER(struct_anon_16)
