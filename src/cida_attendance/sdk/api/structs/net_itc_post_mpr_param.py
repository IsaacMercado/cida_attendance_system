from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_itc_lane_mpr_param import NET_ITC_LANE_MPR_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_ITC_POST_MPR_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_MPR_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('bySourceType', BYTE),
    ('byPicUploadType', BYTE),
    ('byRoadType', BYTE),
    ('byRes2', BYTE),
    ('wCustomDelayTime', WORD),
    ('byRes', BYTE * 56),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLaneParam', NET_ITC_LANE_MPR_PARAM * 6),
    ('szSceneName', c_char * 32),
    ('struSnapLine', NET_VCA_LINE),
    ('byRes1', BYTE * 392),
])

NET_ITC_POST_MPR_PARAM = struct_tagNET_ITC_POST_MPR_PARAM
LPNET_ITC_POST_MPR_PARAM = POINTER(struct_tagNET_ITC_POST_MPR_PARAM)
tagNET_ITC_POST_MPR_PARAM = struct_tagNET_ITC_POST_MPR_PARAM
