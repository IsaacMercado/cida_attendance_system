from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDATE_MODEC(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDATE_MODEC, [
    ('wStartYear', WORD),
    ('byStartMon', BYTE),
    ('byStartDay', BYTE),
    ('wEndYear', WORD),
    ('byEndMon', BYTE),
    ('byEndDay', BYTE),
])

NET_DVR_HOLIDATE_MODEC = struct_tagNET_DVR_HOLIDATE_MODEC
LPNET_DVR_HOLIDATE_MODEC = POINTER(struct_tagNET_DVR_HOLIDATE_MODEC)
tagNET_DVR_HOLIDATE_MODEC = struct_tagNET_DVR_HOLIDATE_MODEC
