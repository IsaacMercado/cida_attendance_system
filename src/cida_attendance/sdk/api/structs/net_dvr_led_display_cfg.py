from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_color_temperature_cfg import NET_DVR_COLOR_TEMPERATURE_CFG
from .net_dvr_video_out_cfg import NET_DVR_VIDEO_OUT_CFG


class struct_tagNET_DVR_LED_DISPLAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_DISPLAY_CFG, [
    ('dwSize', DWORD),
    ('struColorTemp', NET_DVR_COLOR_TEMPERATURE_CFG),
    ('struVoutCfg', NET_DVR_VIDEO_OUT_CFG),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_DISPLAY_CFG = struct_tagNET_DVR_LED_DISPLAY_CFG
LPNET_DVR_LED_DISPLAY_CFG = POINTER(struct_tagNET_DVR_LED_DISPLAY_CFG)
tagNET_DVR_LED_DISPLAY_CFG = struct_tagNET_DVR_LED_DISPLAY_CFG
