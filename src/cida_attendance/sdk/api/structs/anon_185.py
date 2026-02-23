from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_35 import NET_DVR_COMPRESSION_INFO_EX


class struct_anon_185(Structure):
    pass

_S(struct_anon_185, [
    ('dwSize', DWORD),
    ('struLowCompression', NET_DVR_COMPRESSION_INFO_EX),
    ('struEventCompression', NET_DVR_COMPRESSION_INFO_EX),
])

NET_DVR_COMPRESSIONCFG_NEW = struct_anon_185
LPNET_DVR_COMPRESSIONCFG_NEW = POINTER(struct_anon_185)
