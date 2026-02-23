from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_PARKING_CARD(Structure):
    pass

_S(struct_tagNET_DVR_PARKING_CARD, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('szCardNo', c_char * 48),
    ('byCardType', BYTE),
    ('byCardStatus', BYTE),
    ('byChargeRuleID', BYTE),
    ('byDelete', BYTE),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 128),
])

NET_DVR_PARKING_CARD = struct_tagNET_DVR_PARKING_CARD
LPNET_DVR_PARKING_CARD = POINTER(struct_tagNET_DVR_PARKING_CARD)
tagNET_DVR_PARKING_CARD = struct_tagNET_DVR_PARKING_CARD
