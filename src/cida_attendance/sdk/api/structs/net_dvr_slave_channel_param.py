from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_slave_channel_union import NET_DVR_SLAVE_CHANNEL_UNION


class struct_tagNET_DVR_SLAVE_CHANNEL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SLAVE_CHANNEL_PARAM, [
    ('byChanType', BYTE),
    ('byRes1', BYTE * 3),
    ('uSlaveChannel', NET_DVR_SLAVE_CHANNEL_UNION),
    ('byRes2', BYTE * 64),
])

NET_DVR_SLAVE_CHANNEL_PARAM = struct_tagNET_DVR_SLAVE_CHANNEL_PARAM
LPNET_DVR_SLAVE_CHANNEL_PARAM = POINTER(struct_tagNET_DVR_SLAVE_CHANNEL_PARAM)
tagNET_DVR_SLAVE_CHANNEL_PARAM = struct_tagNET_DVR_SLAVE_CHANNEL_PARAM
