from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_READER_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_CARD_READER_CFG_V50, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCardReaderType', BYTE),
    ('byOkLedPolarity', BYTE),
    ('byErrorLedPolarity', BYTE),
    ('byBuzzerPolarity', BYTE),
    ('bySwipeInterval', BYTE),
    ('byPressTimeout', BYTE),
    ('byEnableFailAlarm', BYTE),
    ('byMaxReadCardFailNum', BYTE),
    ('byEnableTamperCheck', BYTE),
    ('byOfflineCheckTime', BYTE),
    ('byFingerPrintCheckLevel', BYTE),
    ('byUseLocalController', BYTE),
    ('byRes1', BYTE),
    ('wLocalControllerID', WORD),
    ('wLocalControllerReaderID', WORD),
    ('wCardReaderChannel', WORD),
    ('byFingerPrintImageQuality', BYTE),
    ('byFingerPrintContrastTimeOut', BYTE),
    ('byFingerPrintRecogizeInterval', BYTE),
    ('byFingerPrintMatchFastMode', BYTE),
    ('byFingerPrintModuleSensitive', BYTE),
    ('byFingerPrintModuleLightCondition', BYTE),
    ('byFaceMatchThresholdN', BYTE),
    ('byFaceQuality', BYTE),
    ('byFaceRecogizeTimeOut', BYTE),
    ('byFaceRecogizeInterval', BYTE),
    ('wCardReaderFunction', WORD),
    ('byCardReaderDescription', BYTE * 32),
    ('wFaceImageSensitometry', WORD),
    ('byLivingBodyDetect', BYTE),
    ('byFaceMatchThreshold1', BYTE),
    ('wBuzzerTime', WORD),
    ('byFaceMatch1SecurityLevel', BYTE),
    ('byFaceMatchNSecurityLevel', BYTE),
    ('byEnvirMode', BYTE),
    ('byLiveDetLevelSet', BYTE),
    ('byLiveDetAntiAttackCntLimit', BYTE),
    ('byEnableLiveDetAntiAttack', BYTE),
    ('bySupportDelFPByID', BYTE),
    ('byFaceContrastMotionDetLevel', BYTE),
    ('byDayFaceMatchThresholdN', BYTE),
    ('byNightFaceMatchThresholdN', BYTE),
    ('byFaceRecogizeEnable', BYTE),
    ('byBlockListMatchThreshold', BYTE),
    ('byRes3', BYTE),
    ('byDefaultVerifyMode', BYTE),
    ('dwFingerPrintCapacity', DWORD),
    ('dwFingerPrintNum', DWORD),
    ('byEnableFingerPrintNum', BYTE),
    ('byEnableReverseCardNo', BYTE),
    ('byRes2', BYTE * 2),
    ('dwIndependSwipeIntervals', DWORD),
    ('byRes', BYTE * 224),
])

NET_DVR_CARD_READER_CFG_V50 = struct_tagNET_DVR_CARD_READER_CFG_V50
LPNET_DVR_CARD_READER_CFG_V50 = POINTER(struct_tagNET_DVR_CARD_READER_CFG_V50)
tagNET_DVR_CARD_READER_CFG_V50 = struct_tagNET_DVR_CARD_READER_CFG_V50
