from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_multi_stream_compressioncfg_cond import (
    NET_DVR_MULTI_STREAM_COMPRESSIONCFG_COND,
)


class struct_tagNET_DVR_MUL_STREAM_CHANNEL_GROUP(Structure):
    pass

_S(struct_tagNET_DVR_MUL_STREAM_CHANNEL_GROUP, [
    ('dwSize', DWORD),
    ('dwGroup', DWORD),
    ('struMultiStreamCfg', NET_DVR_MULTI_STREAM_COMPRESSIONCFG_COND),
    ('byRes', BYTE * 64),
])

NET_DVR_MUL_STREAM_CHANNEL_GROUP = struct_tagNET_DVR_MUL_STREAM_CHANNEL_GROUP
LPNET_DVR_MUL_STREAM_CHANNEL_GROUP = POINTER(struct_tagNET_DVR_MUL_STREAM_CHANNEL_GROUP)
tagNET_DVR_MUL_STREAM_CHANNEL_GROUP = struct_tagNET_DVR_MUL_STREAM_CHANNEL_GROUP
