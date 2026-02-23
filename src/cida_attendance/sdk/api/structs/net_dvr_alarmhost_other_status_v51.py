from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V51(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V51, [
    ('dwSize', DWORD),
    ('bySirenStatus', BYTE * 8),
    ('byDetetorPower', BYTE * 256),
    ('byDetetorConnection', BYTE * 256),
    ('bySirenPower', BYTE * 8),
    ('bySirenTamperStatus', BYTE * 8),
    ('byPowerStausEnabled', BYTE * int((256 / 8))),
    ('byDetetorPowerStatus', BYTE * int((256 / 8))),
    ('byDetetorPowerType', BYTE),
    ('byRes2', BYTE * 3),
    ('byRepeaterStatus', BYTE * 16),
    ('byRepeaterTamperStatus', BYTE * int((16 / 8))),
    ('byAlarmOutTamperStatus', BYTE * int((512 / 8))),
    ('byOutputModuleTamperStatus', BYTE * int((64 / 8))),
    ('byElectricLockStatus', BYTE * 64),
    ('byRes', BYTE * 274),
])

NET_DVR_ALARMHOST_OTHER_STATUS_V51 = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V51
LPNET_DVR_ALARMHOST_OTHER_STATUS_V51 = POINTER(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V51)
tagNET_DVR_ALARMHOST_OTHER_STATUS_V51 = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V51
