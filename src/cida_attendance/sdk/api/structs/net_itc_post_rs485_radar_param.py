from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_param import NET_ITC_LANE_PARAM
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_radar_param import NET_ITC_RADAR_PARAM


class struct_tagNET_ITC_POST_RS485_RADAR_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_RS485_RADAR_PARAM, [
    ('byRelatedLaneNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLane', NET_ITC_LANE_PARAM * 6),
    ('struRadar', NET_ITC_RADAR_PARAM),
    ('byRes', BYTE * 32),
])

NET_ITC_POST_RS485_RADAR_PARAM = struct_tagNET_ITC_POST_RS485_RADAR_PARAM
LPNET_ITC_POST_RS485_RADAR_PARAM = POINTER(struct_tagNET_ITC_POST_RS485_RADAR_PARAM)
tagNET_ITC_POST_RS485_RADAR_PARAM = struct_tagNET_ITC_POST_RS485_RADAR_PARAM
