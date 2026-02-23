from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_input_source_text import NET_DVR_INPUT_SOURCE_TEXT


class struct_tagNET_DVR_INPUT_SOURCE_TEXT_LIST(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SOURCE_TEXT_LIST, [
    ('dwSize', DWORD),
    ('struTextList', NET_DVR_INPUT_SOURCE_TEXT * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_INPUT_SOURCE_TEXT_LIST = struct_tagNET_DVR_INPUT_SOURCE_TEXT_LIST
LPNET_DVR_INPUT_SOURCE_TEXT_LIST = POINTER(struct_tagNET_DVR_INPUT_SOURCE_TEXT_LIST)
tagNET_DVR_INPUT_SOURCE_TEXT_LIST = struct_tagNET_DVR_INPUT_SOURCE_TEXT_LIST
