from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_codedev_info import NET_DVR_CODEDEV_INFO
from .net_dvr_decodedev_info import NET_DVR_DECODEDEV_INFO
from .net_dvr_netsignaldev_info import NET_DVR_NETSIGNALDEV_INFO


class union_tagNET_DVR_DIFFDEV_INFO(Union):
    pass

_S(union_tagNET_DVR_DIFFDEV_INFO, [
    ('struCodeDevInfo', NET_DVR_CODEDEV_INFO),
    ('struDecodeDevInfo', NET_DVR_DECODEDEV_INFO),
    ('struNetSignalInfo', NET_DVR_NETSIGNALDEV_INFO),
])

NET_DVR_DIFFDEV_INFO = union_tagNET_DVR_DIFFDEV_INFO
LPNET_DVR_DIFFDEV_INFO = POINTER(union_tagNET_DVR_DIFFDEV_INFO)
tagNET_DVR_DIFFDEV_INFO = union_tagNET_DVR_DIFFDEV_INFO
