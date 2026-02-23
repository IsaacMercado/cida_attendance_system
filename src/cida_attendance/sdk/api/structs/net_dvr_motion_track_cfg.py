from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MOTION_TRACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MOTION_TRACK_CFG, [
    ('dwSize', DWORD),
    ('byEnableTrack', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_MOTION_TRACK_CFG = struct_tagNET_DVR_MOTION_TRACK_CFG
LPNET_DVR_MOTION_TRACK_CFG = POINTER(struct_tagNET_DVR_MOTION_TRACK_CFG)
tagNET_DVR_MOTION_TRACK_CFG = struct_tagNET_DVR_MOTION_TRACK_CFG
