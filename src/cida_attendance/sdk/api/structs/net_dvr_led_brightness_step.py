from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_BRIGHTNESS_STEP(Structure):
    pass

_S(struct_tagNET_DVR_LED_BRIGHTNESS_STEP, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('byBrightnessStep', BYTE * 48),
    ('byRes2', BYTE * 48),
])

NET_DVR_LED_BRIGHTNESS_STEP = struct_tagNET_DVR_LED_BRIGHTNESS_STEP
LPNET_DVR_LED_BRIGHTNESS_STEP = POINTER(struct_tagNET_DVR_LED_BRIGHTNESS_STEP)
tagNET_DVR_LED_BRIGHTNESS_STEP = struct_tagNET_DVR_LED_BRIGHTNESS_STEP
