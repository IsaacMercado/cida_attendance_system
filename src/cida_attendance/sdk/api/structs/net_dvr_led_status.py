from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_LED_STATUS, [
    ('dwSize', DWORD),
    ('bySwitchState', BYTE),
    ('byBrightness', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_LED_STATUS = struct_tagNET_DVR_LED_STATUS
LPNET_DVR_LED_STATUS = POINTER(struct_tagNET_DVR_LED_STATUS)
tagNET_DVR_LED_STATUS = struct_tagNET_DVR_LED_STATUS
