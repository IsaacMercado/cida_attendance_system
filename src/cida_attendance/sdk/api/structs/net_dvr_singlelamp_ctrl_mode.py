from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_park_external_subinfo import NET_DVR_PARK_EXTERNAL_SUBINFO


class struct_tagNET_DVR_SINGLELAMP_CTRL_MODE(Structure):
    pass

_S(struct_tagNET_DVR_SINGLELAMP_CTRL_MODE, [
    ('struExternLampStateCtrl', NET_DVR_PARK_EXTERNAL_SUBINFO * 8),
    ('byLampType', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_SINGLELAMP_CTRL_MODE = struct_tagNET_DVR_SINGLELAMP_CTRL_MODE
LPNET_DVR_SINGLELAMP_CTRL_MODE = POINTER(struct_tagNET_DVR_SINGLELAMP_CTRL_MODE)
tagNET_DVR_SINGLELAMP_CTRL_MODE = struct_tagNET_DVR_SINGLELAMP_CTRL_MODE
