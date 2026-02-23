from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dev_chan_info import NET_DVR_DEV_CHAN_INFO
from .net_dvr_stream_media_server_cfg import NET_DVR_STREAM_MEDIA_SERVER_CFG


class struct_anon_324(Structure):
    pass

_S(struct_anon_324, [
    ('dwEnable', DWORD),
    ('byType', BYTE),
    ('byRes', BYTE * 3),
    ('streamMediaServerCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO),
    ('sRtspUrl', BYTE * 128),
])

NET_DVR_MATRIX_CHAN_INFO_EX = struct_anon_324
LPNET_DVR_MATRIX_CHAN_INFO_EX = POINTER(struct_anon_324)
