from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_stream_src_info import NET_DVR_STREAM_SRC_INFO


class struct_tagNET_DVR_STREAM_SRC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_SRC_CFG, [
    ('dwSize', DWORD),
    ('struStreamID', NET_DVR_STREAM_INFO),
    ('struStreamSrcInfo', NET_DVR_STREAM_SRC_INFO),
])

NET_DVR_STREAM_SRC_CFG = struct_tagNET_DVR_STREAM_SRC_CFG
LPNET_DVR_STREAM_SRC_CFG = POINTER(struct_tagNET_DVR_STREAM_SRC_CFG)
tagNET_DVR_STREAM_SRC_CFG = struct_tagNET_DVR_STREAM_SRC_CFG
