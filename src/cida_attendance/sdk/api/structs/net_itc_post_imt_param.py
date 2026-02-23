from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_imt_param import NET_ITC_LANE_IMT_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM


class struct_tagNET_ITC_POST_IMT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_IMT_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('bySnapMode', BYTE),
    ('byRes', BYTE * 61),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struLaneParam', NET_ITC_LANE_IMT_PARAM * 6),
    ('byRes1', BYTE * 1584),
])

NET_ITC_POST_IMT_PARAM = struct_tagNET_ITC_POST_IMT_PARAM
LPNET_ITC_POST_IMT_PARAM = POINTER(struct_tagNET_ITC_POST_IMT_PARAM)
tagNET_ITC_POST_IMT_PARAM = struct_tagNET_ITC_POST_IMT_PARAM
