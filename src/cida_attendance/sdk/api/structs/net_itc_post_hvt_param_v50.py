from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_geoglocation import NET_DVR_GEOGLOCATION
from .net_itc_lane_hvt_param_v50 import NET_ITC_LANE_HVT_PARAM_V50
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_POST_HVT_PARAM_V50(Structure):
    pass

_S(struct_tagNET_ITC_POST_HVT_PARAM_V50, [
    ('byLaneNum', BYTE),
    ('byCapType', BYTE),
    ('byCapMode', BYTE),
    ('bySecneMode', BYTE),
    ('bySpeedMode', BYTE),
    ('byLineRuleEffect', BYTE),
    ('byRes1', BYTE * 78),
    ('struLeftTrigLine', NET_ITC_LINE),
    ('struRigtTrigLine', NET_ITC_LINE),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struDetectArea', NET_ITC_POLYGON),
    ('struGeogLocation', NET_DVR_GEOGLOCATION),
    ('struLaneParam', NET_ITC_LANE_HVT_PARAM_V50 * 6),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('byRes2', BYTE * 260),
])

NET_ITC_POST_HVT_PARAM_V50 = struct_tagNET_ITC_POST_HVT_PARAM_V50
LPNET_ITC_POST_HVT_PARAM_V50 = POINTER(struct_tagNET_ITC_POST_HVT_PARAM_V50)
tagNET_ITC_POST_HVT_PARAM_V50 = struct_tagNET_ITC_POST_HVT_PARAM_V50
