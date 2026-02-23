from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_direct_connect_chan_info import NET_DVR_DIRECT_CONNECT_CHAN_INFO
from .net_dvr_pu_stream_url import NET_DVR_PU_STREAM_URL
from .net_dvr_pu_stream_url_cfg import NET_DVR_PU_STREAM_URL_CFG


class union_tagNET_DVR_STREAM_TYPE_UNION(Union):
    pass

_S(union_tagNET_DVR_STREAM_TYPE_UNION, [
    ('struChanInfo', NET_DVR_DIRECT_CONNECT_CHAN_INFO),
    ('struStreamUrl', NET_DVR_PU_STREAM_URL),
    ('struStreamUrlCfg', NET_DVR_PU_STREAM_URL_CFG),
])

NET_DVR_STREAM_TYPE_UNION = union_tagNET_DVR_STREAM_TYPE_UNION
LPNET_DVR_STREAM_TYPE_UNION = POINTER(union_tagNET_DVR_STREAM_TYPE_UNION)
tagNET_DVR_STREAM_TYPE_UNION = union_tagNET_DVR_STREAM_TYPE_UNION
