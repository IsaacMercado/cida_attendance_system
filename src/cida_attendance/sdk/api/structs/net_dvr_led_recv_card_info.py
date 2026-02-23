from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_line_column_info import NET_DVR_LINE_COLUMN_INFO


class struct_tagNET_DVR_LED_RECV_CARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LED_RECV_CARD_INFO, [
    ('struPos', NET_DVR_LINE_COLUMN_INFO),
    ('wRecvCardWidth', WORD),
    ('wRecvCardHeigt', WORD),
])

NET_DVR_LED_RECV_CARD_INFO = struct_tagNET_DVR_LED_RECV_CARD_INFO
LPNET_DVR_LED_RECV_CARD_INFO = POINTER(struct_tagNET_DVR_LED_RECV_CARD_INFO)
tagNET_DVR_LED_RECV_CARD_INFO = struct_tagNET_DVR_LED_RECV_CARD_INFO
