from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_icrtimecfg import NET_ITC_ICRTIMECFG


class struct_tagNET_ITC_ICR_TIMESWITCH_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_ICR_TIMESWITCH_PARAM, [
    ('struAutoCtrlTime', NET_ITC_ICRTIMECFG * 8),
    ('byICRPreset', BYTE * 8),
    ('byRes', BYTE * 20),
])

NET_ITC_ICR_TIMESWITCH_PARAM = struct_tagNET_ITC_ICR_TIMESWITCH_PARAM
LPNET_ITC_ICR_TIMESWITCH_PARAM = POINTER(struct_tagNET_ITC_ICR_TIMESWITCH_PARAM)
tagNET_ITC_ICR_TIMESWITCH_PARAM = struct_tagNET_ITC_ICR_TIMESWITCH_PARAM
