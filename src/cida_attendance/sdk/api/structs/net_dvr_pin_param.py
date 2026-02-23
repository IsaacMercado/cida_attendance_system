from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PIN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PIN_PARAM, [
    ('dwSize', DWORD),
    ('byPIN', BYTE * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_PIN_PARAM = struct_tagNET_DVR_PIN_PARAM
LPNET_DVR_PIN_PARAM = POINTER(struct_tagNET_DVR_PIN_PARAM)
tagNET_DVR_PIN_PARAM = struct_tagNET_DVR_PIN_PARAM
