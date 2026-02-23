from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_151 import struct_anon_151


class struct_anon_152(Structure):
    pass

_S(struct_anon_152, [
    ('byEnableDDNS', BYTE),
    ('byHostIndex', BYTE),
    ('byRes1', BYTE * 2),
    ('struDDNS', struct_anon_151 * 10),
    ('byRes2', BYTE * 16),
])

NET_DVR_DDNSPARA_V30 = struct_anon_152
LPNET_DVR_DDNSPARA_V30 = POINTER(struct_anon_152)
