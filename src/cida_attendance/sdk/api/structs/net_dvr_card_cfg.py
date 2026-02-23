from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_valid_period_cfg import NET_DVR_VALID_PERIOD_CFG


class struct_tagNET_DVR_CARD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CARD_CFG, [
    ('dwSize', DWORD),
    ('dwModifyParamType', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardValid', BYTE),
    ('byCardType', BYTE),
    ('byLeaderCard', BYTE),
    ('byRes1', BYTE),
    ('dwDoorRight', DWORD),
    ('struValid', NET_DVR_VALID_PERIOD_CFG),
    ('dwBelongGroup', DWORD),
    ('byCardPassword', BYTE * 8),
    ('byCardRightPlan', (BYTE * 4) * 32),
    ('dwMaxSwipeTime', DWORD),
    ('dwSwipeTime', DWORD),
    ('wRoomNumber', WORD),
    ('wFloorNumber', SHORT),
    ('byRes2', BYTE * 20),
])

NET_DVR_CARD_CFG = struct_tagNET_DVR_CARD_CFG
LPNET_DVR_CARD_CFG = POINTER(struct_tagNET_DVR_CARD_CFG)
tagNET_DVR_CARD_CFG = struct_tagNET_DVR_CARD_CFG
