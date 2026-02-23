from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_dev_chan_info_v41 import NET_DVR_DEV_CHAN_INFO_V41
from .net_dvr_stream_media_server_cfg_v41 import NET_DVR_STREAM_MEDIA_SERVER_CFG_V41


class struct_tagNET_DVR_DEC_STREAM_DEV(Structure):
    pass

_S(struct_tagNET_DVR_DEC_STREAM_DEV, [
    ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG_V41),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO_V41),
])

NET_DVR_DEC_STREAM_DEV = struct_tagNET_DVR_DEC_STREAM_DEV
LPNET_DVR_DEC_STREAM_DEV = POINTER(struct_tagNET_DVR_DEC_STREAM_DEV)
tagNET_DVR_DEC_STREAM_DEV = struct_tagNET_DVR_DEC_STREAM_DEV
