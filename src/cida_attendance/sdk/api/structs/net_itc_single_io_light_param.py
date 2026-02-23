from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_SINGLE_IO_LIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_IO_LIGHT_PARAM, [
    ('byLightType', BYTE),
    ('byRelatedIO', BYTE),
    ('byRedLightState', BYTE),
    ('byRes', BYTE * 17),
])

NET_ITC_SINGLE_IO_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_IO_LIGHT_PARAM
LPNET_ITC_SINGLE_IO_LIGHT_PARAM = POINTER(struct_tagNET_ITC_SINGLE_IO_LIGHT_PARAM)
tagNET_ITC_SINGLE_IO_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_IO_LIGHT_PARAM
