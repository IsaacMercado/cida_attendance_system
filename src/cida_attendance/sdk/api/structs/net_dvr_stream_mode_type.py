from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_stream_type_union import NET_DVR_STREAM_TYPE_UNION


class struct_tagNET_DVR_STREAM_MODE_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MODE_TYPE, [
    ('byGetStreamType', BYTE),
    ('byRes', BYTE * 3),
    ('uGetStream', NET_DVR_STREAM_TYPE_UNION),
])

NET_DVR_STREAM_MODE_TYPE = struct_tagNET_DVR_STREAM_MODE_TYPE
LPNET_DVR_STREAM_MODE_TYPE = POINTER(struct_tagNET_DVR_STREAM_MODE_TYPE)
tagNET_DVR_STREAM_MODE_TYPE = struct_tagNET_DVR_STREAM_MODE_TYPE
