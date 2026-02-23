from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOOUT_RESOLUTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOOUT_RESOLUTION_CFG, [
    ('dwSize', DWORD),
    ('byResolution', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_VIDEOOUT_RESOLUTION_CFG = struct_tagNET_DVR_VIDEOOUT_RESOLUTION_CFG
LPNET_DVR_VIDEOOUT_RESOLUTION_CFG = POINTER(struct_tagNET_DVR_VIDEOOUT_RESOLUTION_CFG)
tagNET_DVR_VIDEOOUT_RESOLUTION_CFG = struct_tagNET_DVR_VIDEOOUT_RESOLUTION_CFG
