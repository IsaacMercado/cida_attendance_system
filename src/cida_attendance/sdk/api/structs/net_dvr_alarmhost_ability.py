from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ABILITY, [
    ('dwSize', DWORD),
    ('wTotalAlarmInNum', WORD),
    ('wLocalAlarmInNum', WORD),
    ('wExpandAlarmInNum', WORD),
    ('wTotalAlarmOutNum', WORD),
    ('wLocalAlarmOutNum', WORD),
    ('wExpandAlarmOutNum', WORD),
    ('wTotalRs485Num', WORD),
    ('wLocalRs485Num', WORD),
    ('wExpandRs485Num', WORD),
    ('wFullDuplexRs485Num', WORD),
    ('wTotalSensorNum', WORD),
    ('wLocalSensorNum', WORD),
    ('wExpandSensorNum', WORD),
    ('wAudioOutNum', WORD),
    ('wGatewayNum', WORD),
    ('wElectroLockNum', WORD),
    ('wSirenNum', WORD),
    ('wSubSystemNum', WORD),
    ('wNetUserNum', WORD),
    ('wKeyboardNum', WORD),
    ('wOperatorUserNum', WORD),
    ('bySupportDetector', BYTE),
    ('bySupportSensitivity', BYTE),
    ('bySupportArrayBypass', BYTE),
    ('bySupportAlarmInDelay', BYTE),
    ('bySupportAlarmInType', BYTE * 16),
    ('byTelNum', BYTE),
    ('byCenterGroupNum', BYTE),
    ('byGPRSNum', BYTE),
    ('byNetNum', BYTE),
    ('byAudioNum', BYTE),
    ('by3GNum', BYTE),
    ('byAnalogVideoChanNum', BYTE),
    ('byDigitalVideoChanNum', BYTE),
    ('bySubSystemArmType', BYTE),
    ('byPublicSubSystemNum', BYTE),
    ('dwSupport1', DWORD),
    ('dwSubSystemEvent', DWORD),
    ('dwOverallEvent', DWORD),
    ('dwFaultType', DWORD),
    ('byPublicSubsystemAssociateSubsystemNum', BYTE),
    ('byOverallKeyboard', BYTE),
    ('wSafetyCabinSupport', WORD),
    ('by485SlotNum', BYTE),
    ('bySubSystemAttributeAbility', BYTE),
    ('wKeyboardAddrNum', WORD),
    ('byAlarmLampNum', BYTE),
    ('byRes', BYTE * 117),
])

NET_DVR_ALARMHOST_ABILITY = struct_tagNET_DVR_ALARMHOST_ABILITY
LPNET_DVR_ALARMHOST_ABILITY = POINTER(struct_tagNET_DVR_ALARMHOST_ABILITY)
tagNET_DVR_ALARMHOST_ABILITY = struct_tagNET_DVR_ALARMHOST_ABILITY
