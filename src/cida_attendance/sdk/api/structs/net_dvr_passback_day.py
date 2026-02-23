from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PASSBACK_DAY(Structure):
    pass

_S(struct_tagNET_DVR_PASSBACK_DAY, [
    ('byAllDay', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_PASSBACK_DAY = struct_tagNET_DVR_PASSBACK_DAY
LPNET_DVR_PASSBACK_DAY = POINTER(struct_tagNET_DVR_PASSBACK_DAY)
tagNET_DVR_PASSBACK_DAY = struct_tagNET_DVR_PASSBACK_DAY
