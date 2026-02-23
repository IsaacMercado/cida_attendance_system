from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_8 import NET_DVR_HANDLEEXCEPTION


class struct_anon_107(Structure):
    pass

_S(struct_anon_107, [
    ('dwSize', DWORD),
    ('struExceptionHandleType', NET_DVR_HANDLEEXCEPTION * 16),
])

NET_DVR_EXCEPTION = struct_anon_107
LPNET_DVR_EXCEPTION = POINTER(struct_anon_107)
