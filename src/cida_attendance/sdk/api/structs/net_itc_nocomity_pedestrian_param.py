from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_nocomity_pedestrian_param import (
    NET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM,
)
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('byRes', BYTE * 74),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struTriggerLine', NET_ITC_LINE),
    ('struPedesDetRecog', NET_ITC_POLYGON),
    ('struLaneParam', NET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM * 6),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('byRes1', BYTE * 400),
])

NET_ITC_NOCOMITY_PEDESTRIAN_PARAM = struct_tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM
LPNET_ITC_NOCOMITY_PEDESTRIAN_PARAM = POINTER(struct_tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM)
tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM = struct_tagNET_ITC_NOCOMITY_PEDESTRIAN_PARAM
