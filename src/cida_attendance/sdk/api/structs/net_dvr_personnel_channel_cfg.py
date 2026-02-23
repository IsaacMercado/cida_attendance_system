from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PERSONNEL_CHANNEL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PERSONNEL_CHANNEL_CFG, [
    ('dwSize', DWORD),
    ('byInMode', BYTE),
    ('byOutMode', BYTE),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 301),
])

NET_DVR_PERSONNEL_CHANNEL_CFG = struct_tagNET_DVR_PERSONNEL_CHANNEL_CFG
LPNET_DVR_PERSONNEL_CHANNEL_CFG = POINTER(struct_tagNET_DVR_PERSONNEL_CHANNEL_CFG)
tagNET_DVR_PERSONNEL_CHANNEL_CFG = struct_tagNET_DVR_PERSONNEL_CHANNEL_CFG
