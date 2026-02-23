from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_420(Structure):
    pass

_S(struct_anon_420, [
    ('wNetPort', WORD),
    ('byRes', BYTE * 2),
])

NET_DVR_NET_RECEIVE = struct_anon_420
LPNET_DVR_NET_RECEIVE = POINTER(struct_anon_420)
