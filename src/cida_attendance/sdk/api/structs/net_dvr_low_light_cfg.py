from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOW_LIGHT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOW_LIGHT_CFG, [
    ('dwSize', DWORD),
    ('byLowLightLimt', BYTE),
    ('byLowLightLimtLevel', BYTE),
    ('byRes', BYTE * 66),
])

NET_DVR_LOW_LIGHT_CFG = struct_tagNET_DVR_LOW_LIGHT_CFG
LPNET_DVR_LOW_LIGHT_CFG = POINTER(struct_tagNET_DVR_LOW_LIGHT_CFG)
tagNET_DVR_LOW_LIGHT_CFG = struct_tagNET_DVR_LOW_LIGHT_CFG
