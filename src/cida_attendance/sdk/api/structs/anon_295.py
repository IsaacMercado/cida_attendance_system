from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_294 import NET_ITC_HANDLEEXCEPTION


class struct_anon_295(Structure):
    pass

_S(struct_anon_295, [
    ('dwSize', DWORD),
    ('struSnapExceptionType', NET_ITC_HANDLEEXCEPTION * 32),
])

NET_ITC_EXCEPTION = struct_anon_295
LPNET_ITC_EXCEPTION = POINTER(struct_anon_295)
