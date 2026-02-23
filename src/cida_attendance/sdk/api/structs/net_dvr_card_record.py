from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_valid_period_cfg import NET_DVR_VALID_PERIOD_CFG


class struct__NET_DVR_CARD_RECORD(Structure):
    pass

_S(struct__NET_DVR_CARD_RECORD, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardType', BYTE),
    ('byLeaderCard', BYTE),
    ('byUserType', BYTE),
    ('byRes1', BYTE),
    ('byDoorRight', BYTE * 256),
    ('struValid', NET_DVR_VALID_PERIOD_CFG),
    ('byBelongGroup', BYTE * 128),
    ('byCardPassword', BYTE * 8),
    ('wCardRightPlan', WORD * 256),
    ('dwMaxSwipeTimes', DWORD),
    ('dwSwipeTimes', DWORD),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('dwCardRight', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_CARD_RECORD = struct__NET_DVR_CARD_RECORD
LPNET_DVR_CARD_RECORD = POINTER(struct__NET_DVR_CARD_RECORD)
_NET_DVR_CARD_RECORD = struct__NET_DVR_CARD_RECORD
