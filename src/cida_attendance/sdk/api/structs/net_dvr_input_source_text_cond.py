from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_SOURCE_TEXT_COND(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SOURCE_TEXT_COND, [
    ('dwSize', DWORD),
    ('dwInputSourceNo', DWORD),
    ('dwTextNo', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_INPUT_SOURCE_TEXT_COND = struct_tagNET_DVR_INPUT_SOURCE_TEXT_COND
LPNET_DVR_INPUT_SOURCE_TEXT_COND = POINTER(struct_tagNET_DVR_INPUT_SOURCE_TEXT_COND)
tagNET_DVR_INPUT_SOURCE_TEXT_COND = struct_tagNET_DVR_INPUT_SOURCE_TEXT_COND
