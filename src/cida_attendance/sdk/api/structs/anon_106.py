from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_anon_106(Structure):
    pass

_S(struct_anon_106, [
    ('dwSize', DWORD),
    ('struExceptionHandleType', NET_DVR_HANDLEEXCEPTION_V30 * 32),
])

NET_DVR_EXCEPTION_V30 = struct_anon_106
LPNET_DVR_EXCEPTION_V30 = POINTER(struct_anon_106)
