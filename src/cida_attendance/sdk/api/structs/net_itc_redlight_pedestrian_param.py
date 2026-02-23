from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON
from .net_itc_traffic_light_param import NET_ITC_TRAFFIC_LIGHT_PARAM


class struct_tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM, [
    ('byEnable', BYTE),
    ('bySnapNumTimes', BYTE),
    ('byPedesDir', BYTE),
    ('byDelayTime', BYTE),
    ('byStackTargetEnble', BYTE),
    ('byCalibRecogCtrl', BYTE),
    ('byRes1', BYTE * 2),
    ('struTrafficLight', NET_ITC_TRAFFIC_LIGHT_PARAM),
    ('struStopLine', NET_ITC_LINE),
    ('struCalibRecog', NET_ITC_POLYGON * 2),
    ('byRes', BYTE * 440),
])

NET_ITC_REDLIGHT_PEDESTRIAN_PARAM = struct_tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM
LPNET_ITC_REDLIGHT_PEDESTRIAN_PARAM = POINTER(struct_tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM)
tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM = struct_tagNET_ITC_REDLIGHT_PEDESTRIAN_PARAM
