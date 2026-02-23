from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_line import NET_ITC_LINE


class struct_tagNET_ITC_LANE_IMT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_IMT_PARAM, [
    ('byLaneNO', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byRes', BYTE * 146),
    ('struLaneLine', NET_ITC_LINE),
    ('byRes1', BYTE * 256),
])

NET_ITC_LANE_IMT_PARAM = struct_tagNET_ITC_LANE_IMT_PARAM
LPNET_ITC_LANE_IMT_PARAM = POINTER(struct_tagNET_ITC_LANE_IMT_PARAM)
tagNET_ITC_LANE_IMT_PARAM = struct_tagNET_ITC_LANE_IMT_PARAM
