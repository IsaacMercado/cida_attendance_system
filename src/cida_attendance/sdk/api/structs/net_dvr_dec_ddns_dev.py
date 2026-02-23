from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_dev_ddns_info import NET_DVR_DEV_DDNS_INFO
from .net_dvr_stream_media_server import NET_DVR_STREAM_MEDIA_SERVER


class struct_tagNET_DVR_DEC_DDNS_DEV(Structure):
    pass

_S(struct_tagNET_DVR_DEC_DDNS_DEV, [
    ('struDdnsInfo', NET_DVR_DEV_DDNS_INFO),
    ('struMediaServer', NET_DVR_STREAM_MEDIA_SERVER),
])

NET_DVR_DEC_DDNS_DEV = struct_tagNET_DVR_DEC_DDNS_DEV
LPNET_DVR_DEC_DDNS_DEV = POINTER(struct_tagNET_DVR_DEC_DDNS_DEV)
tagNET_DVR_DEC_DDNS_DEV = struct_tagNET_DVR_DEC_DDNS_DEV
