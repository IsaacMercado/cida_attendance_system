from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_339 import union_anon_339
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_LANE_MPR_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_MPR_PARAM, [
    ('byLaneNO', BYTE),
    ('uTssParamInfo', union_anon_339),
    ('byCarDriveDirect', BYTE),
    ('byRes', BYTE * 58),
    ('struLaneLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRelaLaneDirectionType', BYTE),
    ('byRes1', BYTE * 254),
])

NET_ITC_LANE_MPR_PARAM = struct_tagNET_ITC_LANE_MPR_PARAM
LPNET_ITC_LANE_MPR_PARAM = POINTER(struct_tagNET_ITC_LANE_MPR_PARAM)
tagNET_ITC_LANE_MPR_PARAM = struct_tagNET_ITC_LANE_MPR_PARAM
