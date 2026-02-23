from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarmstrategy_param import NET_DVR_ALARMSTRATEGY_PARAM
from .net_dvr_smokedetection_cfg import NET_DVR_SMOKEDETECTION_CFG


class struct_tagNET_DVR_FIREDETECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FIREDETECTION_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('bySensitivity', BYTE),
    ('byFireComfirmTime', BYTE),
    ('byFireRegionOverlay', BYTE),
    ('byDetectionMode', BYTE),
    ('byFireFocusMode', BYTE),
    ('byFireZoomMode', BYTE),
    ('byFirezoomLevel', BYTE),
    ('bySmokeFireEnabled', BYTE),
    ('byFireManualWaitEnabled', BYTE),
    ('byCancelRepeatedAlarmEnabled', BYTE),
    ('byApplicationSceneMode', BYTE),
    ('dwInstallationHeight', DWORD),
    ('byFireSourceDetection', BYTE),
    ('bySmokeAuxiliaryDetectionEnabled', BYTE),
    ('byverificationSensitivity', BYTE),
    ('byFireAlgorithmMode', BYTE),
    ('byAgriculturalMachineryFilterEnabled', BYTE),
    ('byWaterReflectionEnabled', BYTE),
    ('byPatrolSensitivity', BYTE),
    ('byRes', BYTE * 33),
    ('struAlarmStrategy', NET_DVR_ALARMSTRATEGY_PARAM),
    ('struSmokeCfg', NET_DVR_SMOKEDETECTION_CFG),
])

NET_DVR_FIREDETECTION_CFG = struct_tagNET_DVR_FIREDETECTION_CFG
LPNET_DVR_FIREDETECTION_CFG = POINTER(struct_tagNET_DVR_FIREDETECTION_CFG)
tagNET_DVR_FIREDETECTION_CFG = struct_tagNET_DVR_FIREDETECTION_CFG
