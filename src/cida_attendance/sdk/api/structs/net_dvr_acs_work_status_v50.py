from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_WORK_STATUS_V50(Structure):
    pass

_S(struct_tagNET_DVR_ACS_WORK_STATUS_V50, [
    ('dwSize', DWORD),
    ('byDoorLockStatus', BYTE * 256),
    ('byDoorStatus', BYTE * 256),
    ('byMagneticStatus', BYTE * 256),
    ('byCaseStatus', BYTE * 8),
    ('wBatteryVoltage', WORD),
    ('byBatteryLowVoltage', BYTE),
    ('byPowerSupplyStatus', BYTE),
    ('byMultiDoorInterlockStatus', BYTE),
    ('byAntiSneakStatus', BYTE),
    ('byHostAntiDismantleStatus', BYTE),
    ('byIndicatorLightStatus', BYTE),
    ('byCardReaderOnlineStatus', BYTE * 512),
    ('byCardReaderAntiDismantleStatus', BYTE * 512),
    ('byCardReaderVerifyMode', BYTE * 512),
    ('bySetupAlarmStatus', BYTE * 512),
    ('byAlarmInStatus', BYTE * 512),
    ('byAlarmOutStatus', BYTE * 512),
    ('dwCardNum', DWORD),
    ('byFireAlarmStatus', BYTE),
    ('byBatteryChargeStatus', BYTE),
    ('byMasterChannelControllerStatus', BYTE),
    ('bySlaveChannelControllerStatus', BYTE),
    ('byAntiSneakServerStatus', BYTE),
    ('byRes3', BYTE * 3),
    ('dwAllowFaceNum', DWORD),
    ('dwBlockFaceNum', DWORD),
    ('byRes2', BYTE * 108),
])

NET_DVR_ACS_WORK_STATUS_V50 = struct_tagNET_DVR_ACS_WORK_STATUS_V50
LPNET_DVR_ACS_WORK_STATUS_V50 = POINTER(struct_tagNET_DVR_ACS_WORK_STATUS_V50)
tagNET_DVR_ACS_WORK_STATUS_V50 = struct_tagNET_DVR_ACS_WORK_STATUS_V50
