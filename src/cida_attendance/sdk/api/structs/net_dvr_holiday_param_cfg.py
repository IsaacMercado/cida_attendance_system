from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_holiday_param import NET_DVR_HOLIDAY_PARAM


class struct_tagNET_DVR_HOLIDAY_PARAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_PARAM_CFG, [
    ('dwSize', DWORD),
    ('struHolidayParam', NET_DVR_HOLIDAY_PARAM * 32),
    ('byRes', DWORD * 40),
])

NET_DVR_HOLIDAY_PARAM_CFG = struct_tagNET_DVR_HOLIDAY_PARAM_CFG
LPNET_DVR_HOLIDAY_PARAM_CFG = POINTER(struct_tagNET_DVR_HOLIDAY_PARAM_CFG)
tagNET_DVR_HOLIDAY_PARAM_CFG = struct_tagNET_DVR_HOLIDAY_PARAM_CFG
