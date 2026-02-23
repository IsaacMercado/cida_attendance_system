from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_array_info import NET_DVR_ARRAY_INFO


class struct_tagNET_DVR_ARRAY_LIST(Structure):
    pass

_S(struct_tagNET_DVR_ARRAY_LIST, [
    ('dwSize', DWORD),
    ('dwCount', DWORD),
    ('struArrayInfo', NET_DVR_ARRAY_INFO * 8),
])

NET_DVR_ARRAY_LIST = struct_tagNET_DVR_ARRAY_LIST
LPNET_DVR_ARRAY_LIST = POINTER(struct_tagNET_DVR_ARRAY_LIST)
tagNET_DVR_ARRAY_LIST = struct_tagNET_DVR_ARRAY_LIST
