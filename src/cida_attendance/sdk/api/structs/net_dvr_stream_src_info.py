from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_mode_type import NET_DVR_STREAM_MODE_TYPE


class struct_tagNET_DVR_STREAM_SRC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_SRC_INFO, [
    ('dwSize', DWORD),
    ('struStreamSrcInfo', NET_DVR_STREAM_MODE_TYPE),
])

NET_DVR_STREAM_SRC_INFO = struct_tagNET_DVR_STREAM_SRC_INFO
LPNET_DVR_STREAM_SRC_INFO = POINTER(struct_tagNET_DVR_STREAM_SRC_INFO)
tagNET_DVR_STREAM_SRC_INFO = struct_tagNET_DVR_STREAM_SRC_INFO
