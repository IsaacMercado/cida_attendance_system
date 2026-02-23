from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_input_source_resolution import LPNET_DVR_INPUT_SOURCE_RESOLUTION


class struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST, [
    ('dwSize', DWORD),
    ('dwInputSignalCnt', DWORD),
    ('lpstruBuffer', LPNET_DVR_INPUT_SOURCE_RESOLUTION),
    ('dwBufferSize', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_INPUT_SOURCE_RESOLUTION_LIST = struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST
LPNET_DVR_INPUT_SOURCE_RESOLUTION_LIST = POINTER(struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST)
tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST = struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION_LIST
