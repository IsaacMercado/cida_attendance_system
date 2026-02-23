from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_ALARMIN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_PARAM, [
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
    ('byDetectorSerialNo', BYTE * 9),
    ('byZoneSignalType', BYTE),
    ('byDisableDetectorTypeCfg', BYTE),
    ('byTimeOutRange', BYTE),
    ('byAssociateLampOut', BYTE * 8),
    ('wTimeOut', WORD),
    ('byDetectorSignalIntensity', BYTE),
    ('byTimeOutMethod', BYTE),
    ('byRes3', BYTE * 8),
])

NET_DVR_ALARMIN_PARAM = struct_tagNET_DVR_ALARMIN_PARAM
LPNET_DVR_ALARMIN_PARAM = POINTER(struct_tagNET_DVR_ALARMIN_PARAM)
tagNET_DVR_ALARMIN_PARAM = struct_tagNET_DVR_ALARMIN_PARAM
