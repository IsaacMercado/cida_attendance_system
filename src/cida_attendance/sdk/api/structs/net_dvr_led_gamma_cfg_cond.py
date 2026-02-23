from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_line_column_info import NET_DVR_LINE_COLUMN_INFO


class struct_tagNET_DVR_LED_GAMMA_CFG_COND(Structure):
    pass

_S(struct_tagNET_DVR_LED_GAMMA_CFG_COND, [
    ('dwSize', DWORD),
    ('dwOutputNo', DWORD),
    ('struPosStart', NET_DVR_LINE_COLUMN_INFO),
    ('struPosEnd', NET_DVR_LINE_COLUMN_INFO),
    ('byGammaType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_LED_GAMMA_CFG_COND = struct_tagNET_DVR_LED_GAMMA_CFG_COND
LPNET_DVR_LED_GAMMA_CFG_COND = POINTER(struct_tagNET_DVR_LED_GAMMA_CFG_COND)
tagNET_DVR_LED_GAMMA_CFG_COND = struct_tagNET_DVR_LED_GAMMA_CFG_COND
