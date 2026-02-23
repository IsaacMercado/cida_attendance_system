from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_149(Structure):
    pass

_S(struct_anon_149, [
    ('sUsername', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', BYTE * 64),
    ('byEnableDDNS', BYTE),
    ('res', BYTE * 15),
])

NET_DVR_DDNSPARA = struct_anon_149
LPNET_DVR_DDNSPARA = POINTER(struct_anon_149)
