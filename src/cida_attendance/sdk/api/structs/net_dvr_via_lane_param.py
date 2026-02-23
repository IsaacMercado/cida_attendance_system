from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_logic_param import NET_ITC_LANE_LOGIC_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_DVR_VIA_LANE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_VIA_LANE_PARAM, [
    ('byLaneNO', BYTE),
    ('byRes', BYTE * 63),
    ('struLogicParam', NET_ITC_LANE_LOGIC_PARAM),
    ('struLaneLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRes1', BYTE * 300),
])

NET_DVR_VIA_LANE_PARAM = struct_tagNET_DVR_VIA_LANE_PARAM
LPNET_DVR_VIA_LANE_PARAM = POINTER(struct_tagNET_DVR_VIA_LANE_PARAM)
tagNET_DVR_VIA_LANE_PARAM = struct_tagNET_DVR_VIA_LANE_PARAM
