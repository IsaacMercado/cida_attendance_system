from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AIR_CONDITION_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AIR_CONDITION_PARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byMode', BYTE),
    ('byTemperature', BYTE),
    ('byAirConditionNo', BYTE),
    ('byRes', BYTE * 8),
])

NET_DVR_AIR_CONDITION_PARAM = struct_tagNET_DVR_AIR_CONDITION_PARAM
LPNET_DVR_AIR_CONDITION_PARAM = POINTER(struct_tagNET_DVR_AIR_CONDITION_PARAM)
tagNET_DVR_AIR_CONDITION_PARAM = struct_tagNET_DVR_AIR_CONDITION_PARAM
