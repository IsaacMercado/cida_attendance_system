from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LAMP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_INFO, [
    ('byEnable', BYTE),
    ('byFlicker', BYTE),
    ('byLampColor', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_LAMP_INFO = struct_tagNET_DVR_LAMP_INFO
LPNET_DVR_LAMP_INFO = POINTER(struct_tagNET_DVR_LAMP_INFO)
tagNET_DVR_LAMP_INFO = struct_tagNET_DVR_LAMP_INFO
