from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_line_column_info import NET_DVR_LINE_COLUMN_INFO


class struct_tagNET_DVR_LED_CHECK_COND(Structure):
    pass

_S(struct_tagNET_DVR_LED_CHECK_COND, [
    ('dwSize', DWORD),
    ('dwOutputNo', DWORD),
    ('struPosStart', NET_DVR_LINE_COLUMN_INFO),
    ('byStartPosType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwXCoordinate', DWORD),
    ('dwYCoordinate', DWORD),
    ('dwWidth', DWORD),
    ('dwHeight', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_LED_CHECK_COND = struct_tagNET_DVR_LED_CHECK_COND
LPNET_DVR_LED_CHECK_COND = POINTER(struct_tagNET_DVR_LED_CHECK_COND)
tagNET_DVR_LED_CHECK_COND = struct_tagNET_DVR_LED_CHECK_COND
