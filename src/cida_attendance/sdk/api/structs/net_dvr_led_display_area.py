from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_line_column_info import NET_DVR_LINE_COLUMN_INFO


class struct_tagNET_DVR_LED_DISPLAY_AREA(Structure):
    pass

_S(struct_tagNET_DVR_LED_DISPLAY_AREA, [
    ('dwSize', DWORD),
    ('struLCInfo', NET_DVR_LINE_COLUMN_INFO),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('wRecvCardWidth', WORD),
    ('wRecvCardHeigt', WORD),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_DISPLAY_AREA = struct_tagNET_DVR_LED_DISPLAY_AREA
LPNET_DVR_LED_DISPLAY_AREA = POINTER(struct_tagNET_DVR_LED_DISPLAY_AREA)
tagNET_DVR_LED_DISPLAY_AREA = struct_tagNET_DVR_LED_DISPLAY_AREA
