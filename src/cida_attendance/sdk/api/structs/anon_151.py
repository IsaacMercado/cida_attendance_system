from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_151(Structure):
    pass

_S(struct_anon_151, [
    ('sUsername', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', BYTE * 64),
    ('sServerName', BYTE * 64),
    ('wDDNSPort', WORD),
    ('wCountryID', WORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 7),
])

