from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_dev_ip_info import NET_DVR_DEV_IP_INFO


class union_tagNET_DVR_SCREEN_BASE_INFO(Union):
    pass

_S(union_tagNET_DVR_SCREEN_BASE_INFO, [
    ('byScreenAddress', BYTE * 16),
    ('struIPInfo', NET_DVR_DEV_IP_INFO),
    ('byRes', BYTE * 100),
])

NET_DVR_SCREEN_BASE_INFO = union_tagNET_DVR_SCREEN_BASE_INFO
LPNET_DVR_SCREEN_BASE_INFO = POINTER(union_tagNET_DVR_SCREEN_BASE_INFO)
tagNET_DVR_SCREEN_BASE_INFO = union_tagNET_DVR_SCREEN_BASE_INFO
