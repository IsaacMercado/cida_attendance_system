from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDAY_GROUP_COND(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_GROUP_COND, [
    ('dwSize', DWORD),
    ('dwHolidayGroupNumber', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 106),
])

NET_DVR_HOLIDAY_GROUP_COND = struct_tagNET_DVR_HOLIDAY_GROUP_COND
LPNET_DVR_HOLIDAY_GROUP_COND = POINTER(struct_tagNET_DVR_HOLIDAY_GROUP_COND)
tagNET_DVR_HOLIDAY_GROUP_COND = struct_tagNET_DVR_HOLIDAY_GROUP_COND
