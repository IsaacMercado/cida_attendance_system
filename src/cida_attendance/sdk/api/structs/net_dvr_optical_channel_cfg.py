from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_optical_channel_bind import NET_DVR_OPTICAL_CHANNEL_BIND


class struct_tagNET_DVR_OPTICAL_CHANNEL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_CHANNEL_CFG, [
    ('dwSize', DWORD),
    ('struBindVideo', NET_DVR_OPTICAL_CHANNEL_BIND),
    ('struBindAudio', NET_DVR_OPTICAL_CHANNEL_BIND),
    ('byRes', BYTE * 16),
])

NET_DVR_OPTICAL_CHANNEL_CFG = struct_tagNET_DVR_OPTICAL_CHANNEL_CFG
LPNET_DVR_OPTICAL_CHANNEL_CFG = POINTER(struct_tagNET_DVR_OPTICAL_CHANNEL_CFG)
tagNET_DVR_OPTICAL_CHANNEL_CFG = struct_tagNET_DVR_OPTICAL_CHANNEL_CFG
