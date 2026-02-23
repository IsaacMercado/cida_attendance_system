from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DOOR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DOOR_CFG, [
    ('dwSize', DWORD),
    ('byDoorName', BYTE * 32),
    ('byMagneticType', BYTE),
    ('byOpenButtonType', BYTE),
    ('byOpenDuration', BYTE),
    ('byAccessibleOpenDuration', BYTE),
    ('byMagneticAlarmTimeout', BYTE),
    ('byEnableDoorLock', BYTE),
    ('byEnableLeaderCard', BYTE),
    ('byLeaderCardMode', BYTE),
    ('dwLeaderCardOpenDuration', DWORD),
    ('byStressPassword', BYTE * 8),
    ('bySuperPassword', BYTE * 8),
    ('byUnlockPassword', BYTE * 8),
    ('byUseLocalController', BYTE),
    ('byRes1', BYTE),
    ('wLocalControllerID', WORD),
    ('wLocalControllerDoorNumber', WORD),
    ('wLocalControllerStatus', WORD),
    ('byLockInputCheck', BYTE),
    ('byLockInputType', BYTE),
    ('byDoorTerminalMode', BYTE),
    ('byOpenButton', BYTE),
    ('byLadderControlDelayTime', BYTE),
    ('byRes2', BYTE * 43),
])

NET_DVR_DOOR_CFG = struct_tagNET_DVR_DOOR_CFG
LPNET_DVR_DOOR_CFG = POINTER(struct_tagNET_DVR_DOOR_CFG)
tagNET_DVR_DOOR_CFG = struct_tagNET_DVR_DOOR_CFG
