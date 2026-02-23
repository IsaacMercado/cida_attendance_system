from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_159(Structure):
    pass

_S(struct_anon_159, [
    ('dwSize', DWORD),
    ('sFirstDNSIP', c_char * 16),
    ('sSecondDNSIP', c_char * 16),
    ('sRes', c_char * 32),
])

NET_DVR_NETCFG_OTHER = struct_anon_159
LPNET_DVR_NETCFG_OTHER = POINTER(struct_anon_159)
