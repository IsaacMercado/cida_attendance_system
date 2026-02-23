from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARK_EXTERNAL_SUBINFO(Structure):
    pass

_S(struct_tagNET_DVR_PARK_EXTERNAL_SUBINFO, [
    ('byEnable', BYTE),
    ('byFlicker', BYTE),
    ('byIOState', BYTE),
    ('byLampColor', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_PARK_EXTERNAL_SUBINFO = struct_tagNET_DVR_PARK_EXTERNAL_SUBINFO
LPNET_DVR_PARK_EXTERNAL_SUBINFO = POINTER(struct_tagNET_DVR_PARK_EXTERNAL_SUBINFO)
tagNET_DVR_PARK_EXTERNAL_SUBINFO = struct_tagNET_DVR_PARK_EXTERNAL_SUBINFO
