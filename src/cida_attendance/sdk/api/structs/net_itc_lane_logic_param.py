from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_LANE_LOGIC_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_LOGIC_PARAM, [
    ('byUseageType', BYTE),
    ('byDirectionType', BYTE),
    ('byCarDriveDirect', BYTE),
    ('byRes', BYTE * 33),
])

NET_ITC_LANE_LOGIC_PARAM = struct_tagNET_ITC_LANE_LOGIC_PARAM
LPNET_ITC_LANE_LOGIC_PARAM = POINTER(struct_tagNET_ITC_LANE_LOGIC_PARAM)
tagNET_ITC_LANE_LOGIC_PARAM = struct_tagNET_ITC_LANE_LOGIC_PARAM
