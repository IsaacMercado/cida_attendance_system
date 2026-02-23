from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM, [
    ('byDetectThreshold', BYTE),
    ('byAbBrightnessThreshold', BYTE),
    ('byRes', BYTE * 154),
])

NET_ITC_ICR_ALGAOTOSWITCH_PARAM = struct_tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM
LPNET_ITC_ICR_ALGAOTOSWITCH_PARAM = POINTER(struct_tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM)
tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM = struct_tagNET_ITC_ICR_ALGAOTOSWITCH_PARAM
