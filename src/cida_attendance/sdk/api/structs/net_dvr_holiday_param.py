from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_holidate_union import NET_DVR_HOLIDATE_UNION


class struct_tagNET_DVR_HOLIDAY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_PARAM, [
    ('byEnable', BYTE),
    ('byDateMode', BYTE),
    ('byRes1', BYTE * 2),
    ('uHolidate', NET_DVR_HOLIDATE_UNION),
    ('byName', BYTE * 32),
    ('byRes2', BYTE * 20),
])

NET_DVR_HOLIDAY_PARAM = struct_tagNET_DVR_HOLIDAY_PARAM
LPNET_DVR_HOLIDAY_PARAM = POINTER(struct_tagNET_DVR_HOLIDAY_PARAM)
tagNET_DVR_HOLIDAY_PARAM = struct_tagNET_DVR_HOLIDAY_PARAM
