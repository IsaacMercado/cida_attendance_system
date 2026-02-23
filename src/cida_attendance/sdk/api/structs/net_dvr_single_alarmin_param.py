from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_ALARMIN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_ALARMIN_PARAM, [
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
    ('byRes3', BYTE * 110),
])

NET_DVR_SINGLE_ALARMIN_PARAM = struct_tagNET_DVR_SINGLE_ALARMIN_PARAM
LPNET_DVR_SINGLE_ALARMIN_PARAM = POINTER(struct_tagNET_DVR_SINGLE_ALARMIN_PARAM)
tagNET_DVR_SINGLE_ALARMIN_PARAM = struct_tagNET_DVR_SINGLE_ALARMIN_PARAM
