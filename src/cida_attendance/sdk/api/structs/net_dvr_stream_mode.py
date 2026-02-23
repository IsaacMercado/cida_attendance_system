from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_get_stream_union import NET_DVR_GET_STREAM_UNION


class struct_tagNET_DVR_STREAM_MODE(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MODE, [
    ('byGetStreamType', BYTE),
    ('byRes', BYTE * 3),
    ('uGetStream', NET_DVR_GET_STREAM_UNION),
])

NET_DVR_STREAM_MODE = struct_tagNET_DVR_STREAM_MODE
LPNET_DVR_STREAM_MODE = POINTER(struct_tagNET_DVR_STREAM_MODE)
tagNET_DVR_STREAM_MODE = struct_tagNET_DVR_STREAM_MODE
