from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_73 import NET_DVR_IPCHANINFO
from .net_dvr_ddns_stream_cfg import NET_DVR_DDNS_STREAM_CFG
from .net_dvr_hkddns_stream import NET_DVR_HKDDNS_STREAM
from .net_dvr_ipchaninfo_v40 import NET_DVR_IPCHANINFO_V40
from .net_dvr_ipserver_stream import NET_DVR_IPSERVER_STREAM
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG
from .net_dvr_pu_stream_url import NET_DVR_PU_STREAM_URL


class union_tagNET_DVR_GET_STREAM_UNION(Union):
    pass

_S(union_tagNET_DVR_GET_STREAM_UNION, [
    ('struChanInfo', NET_DVR_IPCHANINFO),
    ('struIPServerStream', NET_DVR_IPSERVER_STREAM),
    ('struPUStream', NET_DVR_PU_STREAM_CFG),
    ('struDDNSStream', NET_DVR_DDNS_STREAM_CFG),
    ('struStreamUrl', NET_DVR_PU_STREAM_URL),
    ('struHkDDNSStream', NET_DVR_HKDDNS_STREAM),
    ('struIPChan', NET_DVR_IPCHANINFO_V40),
])

NET_DVR_GET_STREAM_UNION = union_tagNET_DVR_GET_STREAM_UNION
LPNET_DVR_GET_STREAM_UNION = POINTER(union_tagNET_DVR_GET_STREAM_UNION)
tagNET_DVR_GET_STREAM_UNION = union_tagNET_DVR_GET_STREAM_UNION
