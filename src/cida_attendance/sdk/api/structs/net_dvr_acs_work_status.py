from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_WORK_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_ACS_WORK_STATUS, [
    ('dwSize', DWORD),
    ('byDoorLockStatus', BYTE * 32),
    ('byDoorStatus', BYTE * 32),
    ('byMagneticStatus', BYTE * 32),
    ('byCaseStatus', BYTE * 8),
    ('wBatteryVoltage', WORD),
    ('byBatteryLowVoltage', BYTE),
    ('byPowerSupplyStatus', BYTE),
    ('byMultiDoorInterlockStatus', BYTE),
    ('byAntiSneakStatus', BYTE),
    ('byHostAntiDismantleStatus', BYTE),
    ('byIndicatorLightStatus', BYTE),
    ('byCardReaderOnlineStatus', BYTE * 64),
    ('byCardReaderAntiDismantleStatus', BYTE * 64),
    ('byCardReaderVerifyMode', BYTE * 64),
    ('bySetupAlarmStatus', BYTE * 512),
    ('byAlarmInStatus', BYTE * 512),
    ('byAlarmOutStatus', BYTE * 512),
    ('dwCardNum', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_ACS_WORK_STATUS = struct_tagNET_DVR_ACS_WORK_STATUS
LPNET_DVR_ACS_WORK_STATUS = POINTER(struct_tagNET_DVR_ACS_WORK_STATUS)
tagNET_DVR_ACS_WORK_STATUS = struct_tagNET_DVR_ACS_WORK_STATUS
