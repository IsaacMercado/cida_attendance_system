from ctypes import Structure

from ..base_classes import _S, DWORD
from .net_dvr_stream_media_server_cfg import NET_DVR_STREAM_MEDIA_SERVER_CFG
from .net_matrix_dev_chan_info import NET_MATRIX_DEV_CHAN_INFO


class struct_tagNET_MATRIX_PU_STREAM_CFG(Structure):
    pass

_S(struct_tagNET_MATRIX_PU_STREAM_CFG, [
    ('dwSize', DWORD),
    ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
    ('struDevChanInfo', NET_MATRIX_DEV_CHAN_INFO),
])

NET_MATRIX_PU_STREAM_CFG = struct_tagNET_MATRIX_PU_STREAM_CFG
LPNET_MATRIX_PU_STREAM_CFG = struct_tagNET_MATRIX_PU_STREAM_CFG
tagNET_MATRIX_PU_STREAM_CFG = struct_tagNET_MATRIX_PU_STREAM_CFG
