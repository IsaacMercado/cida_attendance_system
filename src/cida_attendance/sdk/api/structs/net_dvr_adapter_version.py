from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ADAPTER_VERSION(Structure):
    pass

_S(struct_tagNET_DVR_ADAPTER_VERSION, [
    ('wMajorVersion', WORD),
    ('wMinorVersion', WORD),
    ('wRevisionNumber', WORD),
    ('wBuildNumber', WORD),
])

NET_DVR_ADAPTER_VERSION = struct_tagNET_DVR_ADAPTER_VERSION
LPNET_DVR_ADAPTER_VERSION = POINTER(struct_tagNET_DVR_ADAPTER_VERSION)
tagNET_DVR_ADAPTER_VERSION = struct_tagNET_DVR_ADAPTER_VERSION
