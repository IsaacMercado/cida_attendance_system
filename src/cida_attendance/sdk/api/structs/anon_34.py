from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_33 import NET_DVR_COMPRESSION_INFO


class struct_anon_34(Structure):
    pass

_S(struct_anon_34, [
    ('dwSize', DWORD),
    ('struRecordPara', NET_DVR_COMPRESSION_INFO),
    ('struNetPara', NET_DVR_COMPRESSION_INFO),
])

NET_DVR_COMPRESSIONCFG = struct_anon_34
LPNET_DVR_COMPRESSIONCFG = POINTER(struct_anon_34)
