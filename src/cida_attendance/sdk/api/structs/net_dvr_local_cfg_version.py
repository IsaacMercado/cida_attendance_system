from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_CFG_VERSION(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_CFG_VERSION, [
    ('byVersion', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LOCAL_CFG_VERSION = struct_tagNET_DVR_LOCAL_CFG_VERSION
LPNET_DVR_LOCAL_CFG_VERSION = POINTER(struct_tagNET_DVR_LOCAL_CFG_VERSION)
tagNET_DVR_LOCAL_CFG_VERSION = struct_tagNET_DVR_LOCAL_CFG_VERSION
