from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_dec_ddns_dev import NET_DVR_DEC_DDNS_DEV
from .net_dvr_dec_stream_dev_ex import NET_DVR_DEC_STREAM_DEV_EX
from .net_dvr_pu_stream_url import NET_DVR_PU_STREAM_URL


class union_tagNET_DVR_DEC_STREAM_MODE(Union):
    pass

_S(union_tagNET_DVR_DEC_STREAM_MODE, [
    ('struDecStreamDev', NET_DVR_DEC_STREAM_DEV_EX),
    ('struUrlInfo', NET_DVR_PU_STREAM_URL),
    ('struDdnsDecInfo', NET_DVR_DEC_DDNS_DEV),
    ('byRes', BYTE * 300),
])

NET_DVR_DEC_STREAM_MODE = union_tagNET_DVR_DEC_STREAM_MODE
LPNET_DVR_DEC_STREAM_MODE = POINTER(union_tagNET_DVR_DEC_STREAM_MODE)
tagNET_DVR_DEC_STREAM_MODE = union_tagNET_DVR_DEC_STREAM_MODE
