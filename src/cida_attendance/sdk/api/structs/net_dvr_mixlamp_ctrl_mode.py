from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_builtin_parklamp import NET_DVR_BUILTIN_PARKLAMP
from .net_dvr_external_parklamp import NET_DVR_EXTERNAL_PARKLAMP


class struct_tagNET_DVR_MIXLAMP_CTRL_MODE(Structure):
    pass

_S(struct_tagNET_DVR_MIXLAMP_CTRL_MODE, [
    ('struExternalParkLamp', NET_DVR_EXTERNAL_PARKLAMP * 4),
    ('struBuiltInParkLamp', NET_DVR_BUILTIN_PARKLAMP * 8),
])

NET_DVR_MIXLAMP_CTRL_MODE = struct_tagNET_DVR_MIXLAMP_CTRL_MODE
LPNET_DVR_MIXLAMP_CTRL_MODE = POINTER(struct_tagNET_DVR_MIXLAMP_CTRL_MODE)
tagNET_DVR_MIXLAMP_CTRL_MODE = struct_tagNET_DVR_MIXLAMP_CTRL_MODE
