from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_dev_chan_info import NET_DVR_DEV_CHAN_INFO
from .net_dvr_stream_media_server_cfg import NET_DVR_STREAM_MEDIA_SERVER_CFG
from .net_matrix_passivemode import NET_DVR_MATRIX_PASSIVEMODE


class struct_tagDEC_MATRIX_CHAN_INFO(Structure):
    pass

_S(struct_tagDEC_MATRIX_CHAN_INFO, [
    ('dwSize', DWORD),
    ('streamMediaServerCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO),
    ('dwDecState', DWORD),
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
    ('sFileName', c_char * 128),
    ('dwGetStreamMode', DWORD),
    ('struPassiveMode', NET_DVR_MATRIX_PASSIVEMODE),
    ('byRes', BYTE * 32),
])

NET_DVR_MATRIX_DEC_CHAN_INFO_V30 = struct_tagDEC_MATRIX_CHAN_INFO
LPNET_DVR_MATRIX_DEC_CHAN_INFO_V30 = POINTER(struct_tagDEC_MATRIX_CHAN_INFO)
tagDEC_MATRIX_CHAN_INFO = struct_tagDEC_MATRIX_CHAN_INFO
