from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDAY_GROUP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_GROUP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byGroupName', BYTE * 32),
    ('dwHolidayPlanNo', DWORD * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_HOLIDAY_GROUP_CFG = struct_tagNET_DVR_HOLIDAY_GROUP_CFG
LPNET_DVR_HOLIDAY_GROUP_CFG = POINTER(struct_tagNET_DVR_HOLIDAY_GROUP_CFG)
tagNET_DVR_HOLIDAY_GROUP_CFG = struct_tagNET_DVR_HOLIDAY_GROUP_CFG
