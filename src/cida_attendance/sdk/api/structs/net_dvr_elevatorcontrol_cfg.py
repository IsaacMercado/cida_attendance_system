from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ELEVATORCONTROL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ELEVATORCONTROL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('byInterfaceType', BYTE),
    ('byRS485Protocol', BYTE),
    ('byNetworkType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_ELEVATORCONTROL_CFG = struct_tagNET_DVR_ELEVATORCONTROL_CFG
LPNET_DVR_ELEVATORCONTROL_CFG = POINTER(struct_tagNET_DVR_ELEVATORCONTROL_CFG)
tagNET_DVR_ELEVATORCONTROL_CFG = struct_tagNET_DVR_ELEVATORCONTROL_CFG
