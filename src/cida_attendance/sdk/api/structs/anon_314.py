from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_32 import NET_DVR_COMPRESSIONCFG_V30


class struct_anon_314(Structure):
    pass

_S(struct_anon_314, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byCompressType', BYTE),
    ('byRes', BYTE * 15),
    ('struCurrentCfg', NET_DVR_COMPRESSIONCFG_V30),
])

NET_DVR_COMPRESSION_LIMIT = struct_anon_314
LPNET_DVR_COMPRESSION_LIMIT = POINTER(struct_anon_314)
