from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_vtlane_param import NET_ITC_VTLANE_PARAM
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_ITC_VTCOIL_INFO(Structure):
    pass

_S(struct_tagNET_ITC_VTCOIL_INFO, [
    ('struLaneRect', NET_VCA_RECT),
    ('byTrigFlag', BYTE),
    ('byTrigSensitive', BYTE),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byLaneType', BYTE),
    ('byEnableRadar', BYTE),
    ('struLane', NET_ITC_VTLANE_PARAM),
    ('byUseageType', BYTE),
    ('byCarDriveDirect', BYTE),
    ('byRes', BYTE * 30),
])

NET_ITC_VTCOIL_INFO = struct_tagNET_ITC_VTCOIL_INFO
LPNET_ITC_VTCOIL_INFO = POINTER(struct_tagNET_ITC_VTCOIL_INFO)
tagNET_ITC_VTCOIL_INFO = struct_tagNET_ITC_VTCOIL_INFO
