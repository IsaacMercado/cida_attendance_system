from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DECODEDEV_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DECODEDEV_INFO, [
    ('byRes', BYTE * 1408),
])

NET_DVR_DECODEDEV_INFO = struct_tagNET_DVR_DECODEDEV_INFO
LPNET_DVR_DECODEDEV_INFO = POINTER(struct_tagNET_DVR_DECODEDEV_INFO)
tagNET_DVR_DECODEDEV_INFO = struct_tagNET_DVR_DECODEDEV_INFO
