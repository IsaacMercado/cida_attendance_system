from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_31 import NET_DVR_COMPRESSION_INFO_V30


class struct_tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG, [
    ('dwSize', DWORD),
    ('dwStreamType', DWORD),
    ('struStreamPara', NET_DVR_COMPRESSION_INFO_V30),
    ('dwResolution', DWORD),
    ('byRes', BYTE * 76),
])

NET_DVR_MULTI_STREAM_COMPRESSIONCFG = struct_tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG
LPNET_DVR_MULTI_STREAM_COMPRESSIONCFG = POINTER(struct_tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG)
tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG = struct_tagNET_DVR_MULTI_STREAM_COMPRESSIONCFG
