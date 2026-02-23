from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_valid_period_cfg import NET_DVR_VALID_PERIOD_CFG


class struct_tagNET_DVR_CARD_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_CARD_CFG_V50, [
    ('dwSize', DWORD),
    ('dwModifyParamType', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardValid', BYTE),
    ('byCardType', BYTE),
    ('byLeaderCard', BYTE),
    ('byUserType', BYTE),
    ('byDoorRight', BYTE * 256),
    ('struValid', NET_DVR_VALID_PERIOD_CFG),
    ('byBelongGroup', BYTE * 128),
    ('byCardPassword', BYTE * 8),
    ('wCardRightPlan', (WORD * 4) * 256),
    ('dwMaxSwipeTime', DWORD),
    ('dwSwipeTime', DWORD),
    ('wRoomNumber', WORD),
    ('wFloorNumber', SHORT),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('wDepartmentNo', WORD),
    ('wSchedulePlanNo', WORD),
    ('bySchedulePlanType', BYTE),
    ('byRightType', BYTE),
    ('byRes2', BYTE * 2),
    ('dwLockID', DWORD),
    ('byLockCode', BYTE * 8),
    ('byRoomCode', BYTE * 8),
    ('dwCardRight', DWORD),
    ('dwPlanTemplate', DWORD),
    ('dwCardUserId', DWORD),
    ('byCardModelType', BYTE),
    ('byRes3', BYTE * 51),
    ('bySIMNum', BYTE * 32),
])

NET_DVR_CARD_CFG_V50 = struct_tagNET_DVR_CARD_CFG_V50
LPNET_DVR_CARD_CFG_V50 = POINTER(struct_tagNET_DVR_CARD_CFG_V50)
tagNET_DVR_CARD_CFG_V50 = struct_tagNET_DVR_CARD_CFG_V50
