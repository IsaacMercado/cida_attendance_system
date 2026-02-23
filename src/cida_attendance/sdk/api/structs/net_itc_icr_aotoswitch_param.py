from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_ICR_AOTOSWITCH_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_ICR_AOTOSWITCH_PARAM, [
    ('byICRPreset', BYTE * 8),
    ('byICRAutoSwitch', BYTE),
    ('byRes', BYTE * 147),
])

NET_ITC_ICR_AOTOSWITCH_PARAM = struct_tagNET_ITC_ICR_AOTOSWITCH_PARAM
LPNET_ITC_ICR_AOTOSWITCH_PARAM = POINTER(struct_tagNET_ITC_ICR_AOTOSWITCH_PARAM)
tagNET_ITC_ICR_AOTOSWITCH_PARAM = struct_tagNET_ITC_ICR_AOTOSWITCH_PARAM
