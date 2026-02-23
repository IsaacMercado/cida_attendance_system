from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_icr_algaotoswitch_param import NET_ITC_ICR_ALGAOTOSWITCH_PARAM
from .net_itc_icr_aotoswitch_param import NET_ITC_ICR_AOTOSWITCH_PARAM
from .net_itc_icr_manualswitch_param import NET_ITC_ICR_MANUALSWITCH_PARAM
from .net_itc_icr_timeswitch_param import NET_ITC_ICR_TIMESWITCH_PARAM


class union_tagNET_ITC_ICR_PARAM_UNION(Union):
    pass

_S(union_tagNET_ITC_ICR_PARAM_UNION, [
    ('uLen', BYTE * 156),
    ('struICRAutoSwitch', NET_ITC_ICR_AOTOSWITCH_PARAM),
    ('struICRManualSwitch', NET_ITC_ICR_MANUALSWITCH_PARAM),
    ('struICRTimeSwitch', NET_ITC_ICR_TIMESWITCH_PARAM),
    ('strICRAlgorithmAutoSwitch', NET_ITC_ICR_ALGAOTOSWITCH_PARAM),
])

NET_ITC_ICR_PARAM_UNION = union_tagNET_ITC_ICR_PARAM_UNION
LPNET_ITC_ICR_PARAM_UNION = POINTER(union_tagNET_ITC_ICR_PARAM_UNION)
tagNET_ITC_ICR_PARAM_UNION = union_tagNET_ITC_ICR_PARAM_UNION
