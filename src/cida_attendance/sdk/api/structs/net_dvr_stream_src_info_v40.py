from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_type_v40_union import NET_DVR_STREAM_TYPE_V40_UNION


class struct_tagNET_DVR_STREAM_SRC_INFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_SRC_INFO_V40, [
    ('dwSize', DWORD),
    ('byGetStreamType', BYTE),
    ('byRes1', BYTE * 3),
    ('uGetStream', NET_DVR_STREAM_TYPE_V40_UNION),
    ('byMonitorName', BYTE * 128),
    ('byRes', BYTE * 384),
])

NET_DVR_STREAM_SRC_INFO_V40 = struct_tagNET_DVR_STREAM_SRC_INFO_V40
LPNET_DVR_STREAM_SRC_INFO_V40 = POINTER(struct_tagNET_DVR_STREAM_SRC_INFO_V40)
tagNET_DVR_STREAM_SRC_INFO_V40 = struct_tagNET_DVR_STREAM_SRC_INFO_V40
