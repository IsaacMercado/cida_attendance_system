from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDATE_MODEB(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDATE_MODEB, [
    ('byStartMonth', BYTE),
    ('byStartWeekNum', BYTE),
    ('byStartWeekday', BYTE),
    ('byEndMonth', BYTE),
    ('byEndWeekNum', BYTE),
    ('byEndWeekday', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_HOLIDATE_MODEB = struct_tagNET_DVR_HOLIDATE_MODEB
LPNET_DVR_HOLIDATE_MODEB = POINTER(struct_tagNET_DVR_HOLIDATE_MODEB)
tagNET_DVR_HOLIDATE_MODEB = struct_tagNET_DVR_HOLIDATE_MODEB
