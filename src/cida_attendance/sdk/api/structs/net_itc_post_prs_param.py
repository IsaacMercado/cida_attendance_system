from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_prs_param import NET_ITC_LANE_PRS_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM


class struct_tagNET_ITC_POST_PRS_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_PRS_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('bySourceType', BYTE),
    ('bySnapMode', BYTE),
    ('byCapMode', BYTE),
    ('byNoPlatCarCap', BYTE),
    ('bySceneMode', BYTE),
    ('byRes', BYTE * 57),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLaneParam', NET_ITC_LANE_PRS_PARAM * 6),
    ('byRes1', BYTE * 440),
])

NET_ITC_POST_PRS_PARAM = struct_tagNET_ITC_POST_PRS_PARAM
LPNET_ITC_POST_PRS_PARAM = POINTER(struct_tagNET_ITC_POST_PRS_PARAM)
tagNET_ITC_POST_PRS_PARAM = struct_tagNET_ITC_POST_PRS_PARAM
