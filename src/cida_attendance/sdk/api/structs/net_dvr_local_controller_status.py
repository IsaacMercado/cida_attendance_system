from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS, [
    ('dwSize', DWORD),
    ('wLocalControllerID', WORD),
    ('byLocalAntiDismantleStatus', BYTE),
    ('byPowerSupplyStatus', BYTE),
    ('wBatteryVoltage', WORD),
    ('byBatteryLowVoltage', BYTE),
    ('byFireAlarm', BYTE),
    ('bySerialNumber', BYTE * 48),
    ('byMagneticStatus', BYTE * 32),
    ('byDoorLockStatus', BYTE * 32),
    ('byCardReaderOnlineStatus', BYTE * 64),
    ('wLocalControllerStatus', WORD),
    ('byRes2', BYTE * 122),
])

NET_DVR_LOCAL_CONTROLLER_STATUS = struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS
LPNET_DVR_LOCAL_CONTROLLER_STATUS = POINTER(struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS)
tagNET_DVR_LOCAL_CONTROLLER_STATUS = struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS
