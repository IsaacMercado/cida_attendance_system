from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ELEVATORCONTROL_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_ELEVATORCONTROL_CFG_V50, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byNegativeFloor', BYTE),
    ('byInterfaceType', BYTE),
    ('byRS485Protocol', BYTE),
    ('byNetworkType', BYTE),
    ('byElevatorControlType', BYTE),
    ('wServerPort', WORD),
    ('struServerIP', NET_DVR_IPADDR),
    ('sUserName', BYTE * 64),
    ('sPassword', BYTE * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_ELEVATORCONTROL_CFG_V50 = struct_tagNET_DVR_ELEVATORCONTROL_CFG_V50
LPNET_DVR_ELEVATORCONTROL_CFG_V50 = POINTER(struct_tagNET_DVR_ELEVATORCONTROL_CFG_V50)
tagNET_DVR_ELEVATORCONTROL_CFG_V50 = struct_tagNET_DVR_ELEVATORCONTROL_CFG_V50
