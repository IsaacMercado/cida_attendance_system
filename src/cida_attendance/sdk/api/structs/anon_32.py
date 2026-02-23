from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_31 import NET_DVR_COMPRESSION_INFO_V30


class struct_anon_32(Structure):
    pass

_S(struct_anon_32, [
    ('dwSize', DWORD),
    ('struNormHighRecordPara', NET_DVR_COMPRESSION_INFO_V30),
    ('struRes', NET_DVR_COMPRESSION_INFO_V30),
    ('struEventRecordPara', NET_DVR_COMPRESSION_INFO_V30),
    ('struNetPara', NET_DVR_COMPRESSION_INFO_V30),
])

NET_DVR_COMPRESSIONCFG_V30 = struct_anon_32
LPNET_DVR_COMPRESSIONCFG_V30 = POINTER(struct_anon_32)
