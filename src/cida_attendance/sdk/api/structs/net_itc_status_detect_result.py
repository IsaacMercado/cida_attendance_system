from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..enums import ITC_STATUS_DETECT_TYPE
from .net_itc_status_union import NET_ITC_STATUS_UNION


class struct_tagNET_ITC_STATUS_DETECT_RESULT(Structure):
    pass

_S(struct_tagNET_ITC_STATUS_DETECT_RESULT, [
    ('dwStatusType', ITC_STATUS_DETECT_TYPE),
    ('uStatusParam', NET_ITC_STATUS_UNION),
    ('dwHoldTime', DWORD),
    ('byRes', BYTE * 32),
])

NET_ITC_STATUS_DETECT_RESULT = struct_tagNET_ITC_STATUS_DETECT_RESULT
LPNET_ITC_STATUS_DETECT_RESULT = POINTER(struct_tagNET_ITC_STATUS_DETECT_RESULT)
tagNET_ITC_STATUS_DETECT_RESULT = struct_tagNET_ITC_STATUS_DETECT_RESULT
