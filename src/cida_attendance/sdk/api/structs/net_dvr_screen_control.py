from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_control_param import NET_DVR_SCREEN_CONTROL_PARAM


class struct_tagNET_DVR_SCREEN_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_CONTROL, [
    ('dwSize', DWORD),
    ('dwCommand', DWORD),
    ('byProtocol', BYTE),
    ('byRes1', BYTE * 3),
    ('struControlParam', NET_DVR_SCREEN_CONTROL_PARAM),
    ('byRes2', BYTE * 52),
])

NET_DVR_SCREEN_CONTROL = struct_tagNET_DVR_SCREEN_CONTROL
LPNET_DVR_SCREEN_CONTROL = POINTER(struct_tagNET_DVR_SCREEN_CONTROL)
tagNET_DVR_SCREEN_CONTROL = struct_tagNET_DVR_SCREEN_CONTROL
