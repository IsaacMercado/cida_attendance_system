from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dev_chan_info import NET_DVR_DEV_CHAN_INFO
from .net_dvr_stream_media_server_cfg import NET_DVR_STREAM_MEDIA_SERVER_CFG


class struct_anon_176(Structure):
    pass

_S(struct_anon_176, [
    ('dwEnable', DWORD),
    ('streamMediaServerCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO),
])

NET_DVR_MATRIX_CHAN_INFO_V30 = struct_anon_176
LPNET_DVR_CYC_SUR_CHAN_ELE_V30 = POINTER(struct_anon_176)
