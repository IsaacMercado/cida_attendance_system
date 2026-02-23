from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from .anon_2 import NET_DVR_IPADDR


class struct_anon_451(Structure):
    pass

_S(struct_anon_451, [
    ('struIp', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('sProtocolDesc', BYTE * 16),
    ('byMacAddr', BYTE * 6),
    ('byRes', BYTE * 344),
])

