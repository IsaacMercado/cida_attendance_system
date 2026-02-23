from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_102(Structure):
    pass

_S(struct_anon_102, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwLocalRight', DWORD * 32),
    ('dwRemoteRight', DWORD * 32),
    ('sUserIP', c_char * 16),
    ('byMACAddr', BYTE * 6),
])

NET_DVR_USER_INFO = struct_anon_102
LPNET_DVR_USER_INFO = POINTER(struct_anon_102)
