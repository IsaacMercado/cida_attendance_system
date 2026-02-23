from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_geoglocation import NET_DVR_GEOGLOCATION
from .net_itc_hvt_ec_param import NET_ITC_HVT_EC_PARAM
from .net_itc_lane_hvt_param import NET_ITC_LANE_HVT_PARAM
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_polygon import NET_ITC_POLYGON
from .net_itc_snapmode_param import NET_ITC_SNAPMODE_PARAM


class struct_tagNET_ITC_POST_HVT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_HVT_PARAM, [
    ('byLaneNum', BYTE),
    ('bySceneMode', BYTE),
    ('byRoadExpBright', BYTE),
    ('byPlateExpBright', BYTE),
    ('struDetectArea', NET_ITC_POLYGON),
    ('struCapMode', NET_ITC_SNAPMODE_PARAM),
    ('struEcParam', NET_ITC_HVT_EC_PARAM),
    ('struLaneParam', NET_ITC_LANE_HVT_PARAM * 6),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struGeogLocation', NET_DVR_GEOGLOCATION),
    ('byRes', BYTE * 324),
])

NET_ITC_POST_HVT_PARAM = struct_tagNET_ITC_POST_HVT_PARAM
LPNET_ITC_POST_HVT_PARAM = POINTER(struct_tagNET_ITC_POST_HVT_PARAM)
tagNET_ITC_POST_HVT_PARAM = struct_tagNET_ITC_POST_HVT_PARAM
