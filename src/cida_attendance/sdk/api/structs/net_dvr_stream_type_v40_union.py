from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_direct_connect_chan_info_v40 import NET_DVR_DIRECT_CONNECT_CHAN_INFO_V40
from .net_dvr_pu_stream_url import NET_DVR_PU_STREAM_URL
from .net_dvr_pu_stream_url_cfg_v40 import NET_DVR_PU_STREAM_URL_CFG_V40
from .net_dvr_rtsp_protocal_cfg import NET_DVR_RTSP_PROTOCAL_CFG
from .net_dvr_stream_url_v40 import NET_DVR_STREAM_URL_V40


class union_tagNET_DVR_STREAM_TYPE_V40_UNION(Union):
    pass

_S(union_tagNET_DVR_STREAM_TYPE_V40_UNION, [
    ('struChanInfo', NET_DVR_DIRECT_CONNECT_CHAN_INFO_V40),
    ('struPuStreamUrl', NET_DVR_PU_STREAM_URL),
    ('struStreamUrlCfg', NET_DVR_PU_STREAM_URL_CFG_V40),
    ('struRtspCfg', NET_DVR_RTSP_PROTOCAL_CFG),
    ('struStreamUrlV40', NET_DVR_STREAM_URL_V40),
])

NET_DVR_STREAM_TYPE_V40_UNION = union_tagNET_DVR_STREAM_TYPE_V40_UNION
LPNET_DVR_STREAM_TYPE_V40_UNION = POINTER(union_tagNET_DVR_STREAM_TYPE_V40_UNION)
tagNET_DVR_STREAM_TYPE_V40_UNION = union_tagNET_DVR_STREAM_TYPE_V40_UNION
