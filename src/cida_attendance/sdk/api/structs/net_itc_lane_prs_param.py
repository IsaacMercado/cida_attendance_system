from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_342 import union_anon_342
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_LANE_PRS_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_PRS_PARAM, [
    ('byLaneNO', BYTE),
    ('uTssParamInfo', union_anon_342),
    ('byRes', BYTE * 59),
    ('struLaneLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRelaLaneDirectionType', BYTE),
    ('byRes2', BYTE * 3),
    ('struTrigLine', NET_ITC_LINE),
    ('byRes1', BYTE * 228),
])

NET_ITC_LANE_PRS_PARAM = struct_tagNET_ITC_LANE_PRS_PARAM
LPNET_ITC_LANE_PRS_PARAM = POINTER(struct_tagNET_ITC_LANE_PRS_PARAM)
tagNET_ITC_LANE_PRS_PARAM = struct_tagNET_ITC_LANE_PRS_PARAM
