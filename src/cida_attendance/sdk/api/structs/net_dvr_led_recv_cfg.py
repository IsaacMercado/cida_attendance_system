from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_led_clock_cfg import NET_DVR_LED_CLOCK_CFG


class struct_tagNET_DVR_LED_RECV_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_RECV_CFG, [
    ('dwSize', DWORD),
    ('struClockCfg', NET_DVR_LED_CLOCK_CFG),
    ('byGrayLevel', BYTE),
    ('byRefreshRate', BYTE),
    ('byLineScanNum', BYTE),
    ('byRefreshCompleteGrayNum', BYTE),
    ('dwHBlank', DWORD),
    ('dwAfterglowCtrl', DWORD),
    ('dwLineFeedTime', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_LED_RECV_CFG = struct_tagNET_DVR_LED_RECV_CFG
LPNET_DVR_LED_RECV_CFG = POINTER(struct_tagNET_DVR_LED_RECV_CFG)
tagNET_DVR_LED_RECV_CFG = struct_tagNET_DVR_LED_RECV_CFG
