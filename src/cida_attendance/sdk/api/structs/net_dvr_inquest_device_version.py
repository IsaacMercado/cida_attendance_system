from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_DEVICE_VERSION(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_DEVICE_VERSION, [
    ('byMainVersion', BYTE),
    ('bySubVersion', BYTE),
    ('byUpgradeVersion', BYTE),
    ('byCustomizeVersion', BYTE),
    ('byRes', BYTE * 60),
])

NET_DVR_INQUEST_DEVICE_VERSION = struct_tagNET_DVR_INQUEST_DEVICE_VERSION
LPNET_DVR_INQUEST_DEVICE_VERSION = POINTER(struct_tagNET_DVR_INQUEST_DEVICE_VERSION)
tagNET_DVR_INQUEST_DEVICE_VERSION = struct_tagNET_DVR_INQUEST_DEVICE_VERSION
