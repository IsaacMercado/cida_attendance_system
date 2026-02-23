from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from .anon_2 import NET_DVR_IPADDR


class struct_anon_425(Structure):
    pass

_S(struct_anon_425, [
    ('struDevIP', NET_DVR_IPADDR),
    ('wDevPort', WORD),
    ('byRes', BYTE * 510),
])

