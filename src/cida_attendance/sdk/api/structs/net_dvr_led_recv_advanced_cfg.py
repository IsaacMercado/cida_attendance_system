from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_led_recv_registor import NET_DVR_LED_RECV_REGISTOR


class struct_tagNET_DVR_LED_RECV_ADVANCED_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_RECV_ADVANCED_CFG, [
    ('dwSize', DWORD),
    ('struFirstRegistor', NET_DVR_LED_RECV_REGISTOR),
    ('struSecondRegistor', NET_DVR_LED_RECV_REGISTOR),
    ('struThirdRegistor', NET_DVR_LED_RECV_REGISTOR),
    ('byRes2', BYTE * 64),
])

NET_DVR_LED_RECV_ADVANCED_CFG = struct_tagNET_DVR_LED_RECV_ADVANCED_CFG
LPNET_DVR_LED_RECV_ADVANCED_CFG = POINTER(struct_tagNET_DVR_LED_RECV_ADVANCED_CFG)
tagNET_DVR_LED_RECV_ADVANCED_CFG = struct_tagNET_DVR_LED_RECV_ADVANCED_CFG
