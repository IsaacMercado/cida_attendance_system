from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_101(Structure):
    pass

_S(struct_anon_101, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwLocalRight', DWORD * 32),
    ('dwLocalPlaybackRight', DWORD),
    ('dwRemoteRight', DWORD * 32),
    ('dwNetPreviewRight', DWORD),
    ('dwNetPlaybackRight', DWORD),
    ('sUserIP', c_char * 16),
    ('byMACAddr', BYTE * 6),
])

NET_DVR_USER_INFO_EX = struct_anon_101
LPNET_DVR_USER_INFO_EX = POINTER(struct_anon_101)
