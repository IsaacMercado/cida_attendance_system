from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_lane_video_epolice_param import NET_ITC_LANE_VIDEO_EPOLICE_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_traffic_light_param import NET_ITC_TRAFFIC_LIGHT_PARAM


class struct_tagNET_ITC_VIDEO_EPOLICE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_VIDEO_EPOLICE_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('byLogicJudge', BYTE),
    ('byRes1', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struTrafficLight', NET_ITC_TRAFFIC_LIGHT_PARAM),
    ('struLaneParam', NET_ITC_LANE_VIDEO_EPOLICE_PARAM * 6),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struLeftLine', NET_ITC_LINE),
    ('struRightLine', NET_ITC_LINE),
    ('struTopZebraLine', NET_ITC_LINE),
    ('struBotZebraLine', NET_ITC_LINE),
    ('byRes', BYTE * 32),
])

NET_ITC_VIDEO_EPOLICE_PARAM = struct_tagNET_ITC_VIDEO_EPOLICE_PARAM
LPNET_ITC_VIDEO_EPOLICE_PARAM = POINTER(struct_tagNET_ITC_VIDEO_EPOLICE_PARAM)
tagNET_ITC_VIDEO_EPOLICE_PARAM = struct_tagNET_ITC_VIDEO_EPOLICE_PARAM
