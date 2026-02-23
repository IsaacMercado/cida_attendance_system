from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_light_accessparam_union import NET_ITC_LIGHT_ACCESSPARAM_UNION


class struct_tagNET_ITC_TRAFFIC_LIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_TRAFFIC_LIGHT_PARAM, [
    ('bySource', BYTE),
    ('byRes1', BYTE * 3),
    ('struLightAccess', NET_ITC_LIGHT_ACCESSPARAM_UNION),
    ('byRes', BYTE * 32),
])

NET_ITC_TRAFFIC_LIGHT_PARAM = struct_tagNET_ITC_TRAFFIC_LIGHT_PARAM
LPNET_ITC_TRAFFIC_LIGHT_PARAM = POINTER(struct_tagNET_ITC_TRAFFIC_LIGHT_PARAM)
tagNET_ITC_TRAFFIC_LIGHT_PARAM = struct_tagNET_ITC_TRAFFIC_LIGHT_PARAM
