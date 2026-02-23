from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_epolice_lane_param import NET_ITC_EPOLICE_LANE_PARAM
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM


class struct_tagNET_ITC_EPOLICE_RS485_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_EPOLICE_RS485_PARAM, [
    ('byRelatedLaneNum', BYTE),
    ('byTrafficLightSignalSrc', BYTE),
    ('byRes1', BYTE * 2),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLane', NET_ITC_EPOLICE_LANE_PARAM * 6),
    ('byRes', BYTE * 32),
])

NET_ITC_EPOLICE_RS485_PARAM = struct_tagNET_ITC_EPOLICE_RS485_PARAM
LPNET_ITC_EPOLICE_RS485_PARAM = POINTER(struct_tagNET_ITC_EPOLICE_RS485_PARAM)
tagNET_ITC_EPOLICE_RS485_PARAM = struct_tagNET_ITC_EPOLICE_RS485_PARAM
