from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARK_INLAY_SUBINFO(Structure):
    pass

_S(struct_tagNET_DVR_PARK_INLAY_SUBINFO, [
    ('byEnable', BYTE),
    ('byFlicker', BYTE),
    ('byLampColor', BYTE),
    ('byRes', BYTE * 21),
])

NET_DVR_PARK_INLAY_SUBINFO = struct_tagNET_DVR_PARK_INLAY_SUBINFO
LPNET_DVR_PARK_INLAY_SUBINFO = POINTER(struct_tagNET_DVR_PARK_INLAY_SUBINFO)
tagNET_DVR_PARK_INLAY_SUBINFO = struct_tagNET_DVR_PARK_INLAY_SUBINFO
