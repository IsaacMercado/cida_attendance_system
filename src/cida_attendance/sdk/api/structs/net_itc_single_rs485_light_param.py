from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_SINGLE_RS485_LIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_RS485_LIGHT_PARAM, [
    ('byLightType', BYTE),
    ('byRelatedLightChan', BYTE),
    ('byInputLight', BYTE),
    ('byRelatedYLightChan', BYTE),
    ('byRes', BYTE * 16),
])

NET_ITC_SINGLE_RS485_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_RS485_LIGHT_PARAM
LPNET_ITC_SINGLE_RS485_LIGHT_PARAM = POINTER(struct_tagNET_ITC_SINGLE_RS485_LIGHT_PARAM)
tagNET_ITC_SINGLE_RS485_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_RS485_LIGHT_PARAM
