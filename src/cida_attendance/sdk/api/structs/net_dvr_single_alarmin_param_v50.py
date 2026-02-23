from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_ALARMIN_PARAM_V50(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_ALARMIN_PARAM_V50, [
    ('dwSize', DWORD),
    ('wZoneNo', WORD),
    ('byJointSubSystem', BYTE),
    ('byType', BYTE),
    ('byName', BYTE * 32),
    ('wDetectorType', WORD),
    ('wInDelay', WORD),
    ('wOutDelay', WORD),
    ('byAlarmType', BYTE),
    ('byZoneSignalType', BYTE),
    ('byDetectorSerialNo', BYTE * 9),
    ('byDisableDetectorTypeCfg', BYTE),
    ('byTimeOutRange', BYTE),
    ('byDetectorSignalIntensity', BYTE),
    ('wTimeOut', WORD),
    ('byTimeOutMethod', BYTE),
    ('byAssociateFlashLamp', BYTE),
    ('byStayAwayEnabled', BYTE),
    ('bySilentModeEnabled', BYTE),
    ('byRes3', BYTE * 2),
    ('byAssociateAlarmOut', BYTE * 512),
    ('byRes2', BYTE * 128),
])

NET_DVR_SINGLE_ALARMIN_PARAM_V50 = struct_tagNET_DVR_SINGLE_ALARMIN_PARAM_V50
LPNET_DVR_SINGLE_ALARMIN_PARAM_V50 = POINTER(struct_tagNET_DVR_SINGLE_ALARMIN_PARAM_V50)
tagNET_DVR_SINGLE_ALARMIN_PARAM_V50 = struct_tagNET_DVR_SINGLE_ALARMIN_PARAM_V50
