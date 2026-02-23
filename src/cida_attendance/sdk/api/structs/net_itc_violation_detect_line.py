from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_itc_line import NET_ITC_LINE


class struct_tagNET_ITC_VIOLATION_DETECT_LINE(Structure):
    pass

_S(struct_tagNET_ITC_VIOLATION_DETECT_LINE, [
    ('struLaneLine', NET_ITC_LINE),
    ('struStopLine', NET_ITC_LINE),
    ('struRedLightLine', NET_ITC_LINE),
    ('struCancelLine', NET_ITC_LINE),
    ('struWaitLine', NET_ITC_LINE),
    ('struRes', NET_ITC_LINE * 8),
])

NET_ITC_VIOLATION_DETECT_LINE = struct_tagNET_ITC_VIOLATION_DETECT_LINE
LPNET_ITC_VIOLATION_DETECT_LINE = POINTER(struct_tagNET_ITC_VIOLATION_DETECT_LINE)
tagNET_ITC_VIOLATION_DETECT_LINE = struct_tagNET_ITC_VIOLATION_DETECT_LINE
