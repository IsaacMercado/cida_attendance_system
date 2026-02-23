from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ELEVATORCONTROL_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_ELEVATORCONTROL_CFG_V40, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('byInterfaceType', BYTE),
    ('byRS485Protocol', BYTE),
    ('byNetworkType', BYTE),
    ('byRes2', BYTE),
    ('wServerPort', WORD),
    ('struServerIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 256),
])

NET_DVR_ELEVATORCONTROL_CFG_V40 = struct_tagNET_DVR_ELEVATORCONTROL_CFG_V40
LPNET_DVR_ELEVATORCONTROL_CFG_V40 = POINTER(struct_tagNET_DVR_ELEVATORCONTROL_CFG_V40)
tagNET_DVR_ELEVATORCONTROL_CFG_V40 = struct_tagNET_DVR_ELEVATORCONTROL_CFG_V40
