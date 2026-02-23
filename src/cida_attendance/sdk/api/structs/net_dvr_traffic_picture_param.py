from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_TRAFFIC_PICTURE_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_TRAFFIC_PICTURE_PARAM_, [
    ('struRelativeTime', NET_DVR_TIME_V30),
    ('struAbsTime', NET_DVR_TIME_V30),
    ('szPicName', c_char * 64),
    ('byPicType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_TRAFFIC_PICTURE_PARAM = struct_tagNET_DVR_TRAFFIC_PICTURE_PARAM_
LPNET_DVR_TRAFFIC_PICTURE_PARAM = POINTER(struct_tagNET_DVR_TRAFFIC_PICTURE_PARAM_)
tagNET_DVR_TRAFFIC_PICTURE_PARAM_ = struct_tagNET_DVR_TRAFFIC_PICTURE_PARAM_
