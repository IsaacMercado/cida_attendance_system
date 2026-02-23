from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LAMP_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_PARAM, [
    ('byEnable', BYTE),
    ('byFlicker', BYTE),
    ('byLampColor', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_LAMP_PARAM = struct_tagNET_DVR_LAMP_PARAM
LPNET_DVR_LAMP_PARAM = POINTER(struct_tagNET_DVR_LAMP_PARAM)
tagNET_DVR_LAMP_PARAM = struct_tagNET_DVR_LAMP_PARAM
