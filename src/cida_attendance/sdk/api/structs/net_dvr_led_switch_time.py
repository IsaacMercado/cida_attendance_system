from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_switch_time import NET_DVR_SWITCH_TIME


class struct_tagNET_DVR_LED_SWITCH_TIME(Structure):
    pass

_S(struct_tagNET_DVR_LED_SWITCH_TIME, [
    ('dwSize', DWORD),
    ('struTimer', NET_DVR_SWITCH_TIME * 3),
    ('byRes', BYTE * 64),
])

NET_DVR_LED_SWITCH_TIME = struct_tagNET_DVR_LED_SWITCH_TIME
LPNET_DVR_LED_SWITCH_TIME = POINTER(struct_tagNET_DVR_LED_SWITCH_TIME)
tagNET_DVR_LED_SWITCH_TIME = struct_tagNET_DVR_LED_SWITCH_TIME
