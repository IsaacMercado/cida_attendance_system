from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_ALARMIN_PARAM_V50(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_PARAM_V50, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('wDetectorType', WORD),
    ('byType', BYTE),
    ('byUploadAlarmRecoveryReport', BYTE),
    ('dwParam', DWORD),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
    ('byAssociateAlarmOut', BYTE * 512),
    ('byAssociateSirenOut', BYTE * 8),
    ('bySensitivityParam', BYTE),
    ('byArrayBypass', BYTE),
    ('byJointSubSystem', BYTE),
    ('byModuleStatus', BYTE),
    ('wModuleAddress', WORD),
    ('byModuleChan', BYTE),
    ('byModuleType', BYTE),
    ('wZoneIndex', WORD),
    ('wInDelay', WORD),
    ('wOutDelay', WORD),
    ('byAlarmType', BYTE),
    ('byZoneResistor', BYTE),
    ('fZoneResistorManual', c_float),
    ('byDetectorSerialNo', BYTE * 16),
    ('byZoneSignalType', BYTE),
    ('byDisableDetectorTypeCfg', BYTE),
    ('wTimeOut', WORD),
    ('byAssociateLampOut', BYTE * 8),
    ('byVoiceFileName', BYTE * 32),
    ('byTimeOutRange', BYTE),
    ('byDetectorSignalIntensity', BYTE),
    ('byTimeOutMethod', BYTE),
    ('byAssociateFlashLamp', BYTE),
    ('byStayAwayEnabled', BYTE),
    ('bySilentModeEnabled', BYTE),
    ('byRelativeChannel', BYTE * 2),
    ('byDetectorVersion', BYTE * 32),
    ('byDetectorMAC', BYTE * 6),
    ('byLinkageAlarmType', BYTE),
    ('byRes3', BYTE * 465),
])

NET_DVR_ALARMIN_PARAM_V50 = struct_tagNET_DVR_ALARMIN_PARAM_V50
LPNET_DVR_ALARMIN_PARAM_V50 = POINTER(struct_tagNET_DVR_ALARMIN_PARAM_V50)
tagNET_DVR_ALARMIN_PARAM_V50 = struct_tagNET_DVR_ALARMIN_PARAM_V50
