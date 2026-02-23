from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_148 import NET_DVR_NTPPARA
from .anon_149 import NET_DVR_DDNSPARA


class struct_anon_154(Structure):
    pass

_S(struct_anon_154, [
    ('dwSize', DWORD),
    ('sDNSIp', c_char * 16),
    ('struNtpClientParam', NET_DVR_NTPPARA),
    ('struDDNSClientParam', NET_DVR_DDNSPARA),
    ('res', BYTE * 464),
])

NET_DVR_NETAPPCFG = struct_anon_154
LPNET_DVR_NETAPPCFG = POINTER(struct_anon_154)
