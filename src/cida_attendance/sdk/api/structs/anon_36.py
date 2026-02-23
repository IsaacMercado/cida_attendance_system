from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_35 import NET_DVR_COMPRESSION_INFO_EX


class struct_anon_36(Structure):
    pass

_S(struct_anon_36, [
    ('dwSize', DWORD),
    ('struRecordPara', NET_DVR_COMPRESSION_INFO_EX),
    ('struNetPara', NET_DVR_COMPRESSION_INFO_EX),
])

NET_DVR_COMPRESSIONCFG_EX = struct_anon_36
LPNET_DVR_COMPRESSIONCFG_EX = POINTER(struct_anon_36)
