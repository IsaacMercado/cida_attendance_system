from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POE_ADAPTER_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_POE_ADAPTER_TYPE, [
    ('dwSize', DWORD),
    ('byAdapterType', BYTE),
    ('byRes1', BYTE * 127),
])

NET_DVR_POE_ADAPTER_TYPE = struct_tagNET_DVR_POE_ADAPTER_TYPE
LPNET_DVR_POE_ADAPTER_TYPE = POINTER(struct_tagNET_DVR_POE_ADAPTER_TYPE)
tagNET_DVR_POE_ADAPTER_TYPE = struct_tagNET_DVR_POE_ADAPTER_TYPE
