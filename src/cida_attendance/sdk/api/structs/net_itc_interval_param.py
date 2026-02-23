from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_INTERVAL_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_INTERVAL_PARAM, [
    ('byIntervalType', BYTE),
    ('byRes1', BYTE * 3),
    ('wInterval', WORD * 4),
    ('byRes', BYTE * 8),
])

NET_ITC_INTERVAL_PARAM = struct_tagNET_ITC_INTERVAL_PARAM
LPNET_ITC_INTERVAL_PARAM = POINTER(struct_tagNET_ITC_INTERVAL_PARAM)
tagNET_ITC_INTERVAL_PARAM = struct_tagNET_ITC_INTERVAL_PARAM
