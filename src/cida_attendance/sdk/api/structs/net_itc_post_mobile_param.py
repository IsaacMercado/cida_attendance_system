from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_lane_logic_param import NET_ITC_LANE_LOGIC_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_polygon import NET_ITC_POLYGON
from .net_itc_violation_detect_line import NET_ITC_VIOLATION_DETECT_LINE


class struct_tagNET_ITC_POST_MOBILE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_MOBILE_PARAM, [
    ('byEnable', BYTE),
    ('bySceneMode', BYTE),
    ('wExpressWayCapType', WORD),
    ('wUrbanRoadCapType', WORD),
    ('byCapNum', BYTE),
    ('byRecordEnable', BYTE),
    ('dwPreRecordTime', DWORD),
    ('dwOverRecordTime', DWORD),
    ('struLane', NET_ITC_LANE_LOGIC_PARAM),
    ('struPolygon', NET_ITC_POLYGON * 3),
    ('struLine', NET_ITC_VIOLATION_DETECT_LINE * 3),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRes', BYTE * 256),
])

NET_ITC_POST_MOBILE_PARAM = struct_tagNET_ITC_POST_MOBILE_PARAM
LPNET_ITC_POST_MOBILE_PARAM = POINTER(struct_tagNET_ITC_POST_MOBILE_PARAM)
tagNET_ITC_POST_MOBILE_PARAM = struct_tagNET_ITC_POST_MOBILE_PARAM
