from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_led_area_info import LPNET_DVR_LED_AREA_INFO


class struct_tagNET_DVR_LED_AREA_INFO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_LED_AREA_INFO_LIST, [
    ('dwSize', DWORD),
    ('dwLEDAreaNum', DWORD),
    ('lpstruBuffer', LPNET_DVR_LED_AREA_INFO),
    ('dwBufferSize', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_AREA_INFO_LIST = struct_tagNET_DVR_LED_AREA_INFO_LIST
LPNET_DVR_LED_AREA_INFO_LIST = POINTER(struct_tagNET_DVR_LED_AREA_INFO_LIST)
tagNET_DVR_LED_AREA_INFO_LIST = struct_tagNET_DVR_LED_AREA_INFO_LIST
