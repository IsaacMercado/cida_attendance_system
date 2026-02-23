from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_lamp_info import NET_DVR_LAMP_INFO


class struct_tagNET_DVR_PARKLAMP_CTRL_MODE(Structure):
    pass

_S(struct_tagNET_DVR_PARKLAMP_CTRL_MODE, [
    ('struLampInfo', NET_DVR_LAMP_INFO * 8),
    ('byLampType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_PARKLAMP_CTRL_MODE = struct_tagNET_DVR_PARKLAMP_CTRL_MODE
LPNET_DVR_PARKLAMP_CTRL_MODE = POINTER(struct_tagNET_DVR_PARKLAMP_CTRL_MODE)
tagNET_DVR_PARKLAMP_CTRL_MODE = struct_tagNET_DVR_PARKLAMP_CTRL_MODE
