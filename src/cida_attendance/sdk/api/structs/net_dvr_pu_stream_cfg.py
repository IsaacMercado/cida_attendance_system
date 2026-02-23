from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dev_chan_info import NET_DVR_DEV_CHAN_INFO
from .net_dvr_stream_media_server_cfg import NET_DVR_STREAM_MEDIA_SERVER_CFG


class struct_tagNET_DVR_PU_STREAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PU_STREAM_CFG, [
    ('dwSize', DWORD),
    ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO),
])

NET_DVR_PU_STREAM_CFG = struct_tagNET_DVR_PU_STREAM_CFG
LPNET_DVR_PU_STREAM_CFG = POINTER(struct_tagNET_DVR_PU_STREAM_CFG)
tagNET_DVR_PU_STREAM_CFG = struct_tagNET_DVR_PU_STREAM_CFG
