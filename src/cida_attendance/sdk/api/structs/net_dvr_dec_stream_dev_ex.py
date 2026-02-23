from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_dev_chan_info_ex import NET_DVR_DEV_CHAN_INFO_EX
from .net_dvr_stream_media_server import NET_DVR_STREAM_MEDIA_SERVER


class struct_tagNET_DVR_DEC_STREAM_DEV_EX(Structure):
    pass

_S(struct_tagNET_DVR_DEC_STREAM_DEV_EX, [
    ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO_EX),
])

NET_DVR_DEC_STREAM_DEV_EX = struct_tagNET_DVR_DEC_STREAM_DEV_EX
LPNET_DVR_DEC_STREAM_DEV_EX = POINTER(struct_tagNET_DVR_DEC_STREAM_DEV_EX)
tagNET_DVR_DEC_STREAM_DEV_EX = struct_tagNET_DVR_DEC_STREAM_DEV_EX
