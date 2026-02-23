from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_150(Structure):
    pass

_S(struct_anon_150, [
    ('byHostIndex', BYTE),
    ('byEnableDDNS', BYTE),
    ('wDDNSPort', WORD),
    ('sUsername', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', BYTE * 64),
    ('sServerName', BYTE * 64),
    ('byRes', BYTE * 16),
])

NET_DVR_DDNSPARA_EX = struct_anon_150
LPNET_DVR_DDNSPARA_EX = POINTER(struct_anon_150)
