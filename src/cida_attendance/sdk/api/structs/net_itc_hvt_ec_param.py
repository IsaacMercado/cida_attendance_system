from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_HVT_EC_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_HVT_EC_PARAM, [
    ('dwCapShutter', DWORD),
    ('wCapGain', WORD),
    ('byRes', BYTE * 2),
    ('dwDayTimeVideoShutter', DWORD),
    ('wDayTimeVideoGain', WORD),
    ('wNightVideoGain', WORD),
    ('wNightVideoShutter', DWORD),
    ('byRes1', BYTE * 108),
])

NET_ITC_HVT_EC_PARAM = struct_tagNET_ITC_HVT_EC_PARAM
LPNET_ITC_HVT_EC_PARAM = POINTER(struct_tagNET_ITC_HVT_EC_PARAM)
tagNET_ITC_HVT_EC_PARAM = struct_tagNET_ITC_HVT_EC_PARAM
