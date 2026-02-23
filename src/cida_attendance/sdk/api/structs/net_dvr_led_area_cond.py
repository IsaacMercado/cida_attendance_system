from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_AREA_COND(Structure):
    pass

_S(struct_tagNET_DVR_LED_AREA_COND, [
    ('dwSize', DWORD),
    ('dwVideoWallNo', DWORD),
    ('dwLEDAreaNo', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_AREA_COND = struct_tagNET_DVR_LED_AREA_COND
LPNET_DVR_LED_AREA_COND = POINTER(struct_tagNET_DVR_LED_AREA_COND)
tagNET_DVR_LED_AREA_COND = struct_tagNET_DVR_LED_AREA_COND
