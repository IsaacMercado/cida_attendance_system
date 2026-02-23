from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDATE_MODEA(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDATE_MODEA, [
    ('byStartMonth', BYTE),
    ('byStartDay', BYTE),
    ('byEndMonth', BYTE),
    ('byEndDay', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_HOLIDATE_MODEA = struct_tagNET_DVR_HOLIDATE_MODEA
LPNET_DVR_HOLIDATE_MODEA = POINTER(struct_tagNET_DVR_HOLIDATE_MODEA)
tagNET_DVR_HOLIDATE_MODEA = struct_tagNET_DVR_HOLIDATE_MODEA
