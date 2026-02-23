from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_2(Structure):
    pass

_S(struct_anon_2, [
    ('sIpV4', c_char * 16),
    ('byIPv6', BYTE * 128),
])

NET_DVR_IPADDR = struct_anon_2
LPNET_DVR_IPADDR = POINTER(struct_anon_2)
