from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR


class struct_tagNET_DVR_LED_TEST_SIGNAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_TEST_SIGNAL_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('bySignalType', BYTE),
    ('byRes1', BYTE * 2),
    ('struSignalColor', NET_DVR_RGB_COLOR),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_TEST_SIGNAL_CFG = struct_tagNET_DVR_LED_TEST_SIGNAL_CFG
LPNET_DVR_LED_TEST_SIGNAL_CFG = POINTER(struct_tagNET_DVR_LED_TEST_SIGNAL_CFG)
tagNET_DVR_LED_TEST_SIGNAL_CFG = struct_tagNET_DVR_LED_TEST_SIGNAL_CFG
