from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_ptz_info_ex import NET_PTZ_INFO_EX


class struct_tagNET_DVR_PRESET_NAME(Structure):
    pass

_S(struct_tagNET_DVR_PRESET_NAME, [
    ('dwSize', DWORD),
    ('wPresetNum', WORD),
    ('byRes1', BYTE * 2),
    ('byName', c_char * 32),
    ('wPanPos', WORD),
    ('wTiltPos', WORD),
    ('wZoomPos', WORD),
    ('byRes2', BYTE),
    ('byPTZPosExEnable', BYTE),
    ('struPtzPosEx', NET_PTZ_INFO_EX),
    ('byRes', BYTE * 32),
])

NET_DVR_PRESET_NAME = struct_tagNET_DVR_PRESET_NAME
LPNET_DVR_PRESET_NAME = POINTER(struct_tagNET_DVR_PRESET_NAME)
tagNET_DVR_PRESET_NAME = struct_tagNET_DVR_PRESET_NAME
