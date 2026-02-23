from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_chan_info import NET_DVR_CHAN_INFO


class struct_tagNET_DVR_CODEDEV_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CODEDEV_INFO, [
    ('struChanInfo', NET_DVR_CHAN_INFO * 16),
])

NET_DVR_CODEDEV_INFO = struct_tagNET_DVR_CODEDEV_INFO
LPNET_DVR_CODEDEV_INFO = POINTER(struct_tagNET_DVR_CODEDEV_INFO)
tagNET_DVR_CODEDEV_INFO = struct_tagNET_DVR_CODEDEV_INFO
