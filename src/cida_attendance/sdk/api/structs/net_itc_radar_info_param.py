from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_radar_param import NET_ITC_RADAR_PARAM


class struct_tagNET_ITC_RADAR_INFO_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_RADAR_INFO_PARAM, [
    ('struRadarParam', NET_ITC_RADAR_PARAM),
    ('byAssociateLaneNo', BYTE),
    ('byRes', BYTE * 103),
])

NET_ITC_RADAR_INFO_PARAM = struct_tagNET_ITC_RADAR_INFO_PARAM
LPNET_ITC_RADAR_INFO_PARAM = POINTER(struct_tagNET_ITC_RADAR_INFO_PARAM)
tagNET_ITC_RADAR_INFO_PARAM = struct_tagNET_ITC_RADAR_INFO_PARAM
