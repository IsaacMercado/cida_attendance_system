from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_DEV_ABILITY(Structure):
    pass

_S(struct_tagNET_VCA_DEV_ABILITY, [
    ('dwSize', DWORD),
    ('byVCAChanNum', BYTE),
    ('byPlateChanNum', BYTE),
    ('byBBaseChanNum', BYTE),
    ('byBAdvanceChanNum', BYTE),
    ('byBFullChanNum', BYTE),
    ('byATMChanNum', BYTE),
    ('byPDCChanNum', BYTE),
    ('byITSChanNum', BYTE),
    ('byBPrisonChanNum', BYTE),
    ('byFSnapChanNum', BYTE),
    ('byFSnapRecogChanNum', BYTE),
    ('byFRetrievalChanNum', BYTE),
    ('bySupport', BYTE),
    ('byFRecogChanNum', BYTE),
    ('byBPPerimeterChanNum', BYTE),
    ('byTPSChanNum', BYTE),
    ('byTFSChanNum', BYTE),
    ('byFSnapBFullChanNum', BYTE),
    ('byHeatMapChanNum', BYTE),
    ('bySmartVehicleNum', BYTE),
    ('bySmartHVTNum', BYTE),
    ('bySmartNum', BYTE),
    ('byVehicleNum', BYTE),
    ('bySmartRoadDetectionNum', BYTE),
    ('bySmartFaceDetectionNum', BYTE),
    ('bySmartHeatMapNum', BYTE),
    ('byHumanRecognitionNum', BYTE),
    ('byEdcationStudentNum', BYTE),
    ('byRoadDetectionNum', BYTE),
    ('byPersonDensityDetection', BYTE),
    ('bySafetyHelmetDetection', BYTE),
    ('byPerimeterCapture', BYTE),
    ('byHeelPDC', BYTE),
    ('by12MPLiveView', BYTE),
    ('byTeacherBehaviorDetectNum', BYTE),
    ('byMixedTargetDetection', BYTE),
    ('byFaceContrast', BYTE),
    ('byCityManagement', BYTE),
    ('byMixedTargetDetectionSmart', BYTE),
    ('byRes', BYTE),
])

NET_VCA_DEV_ABILITY = struct_tagNET_VCA_DEV_ABILITY
LPNET_VCA_DEV_ABILITY = POINTER(struct_tagNET_VCA_DEV_ABILITY)
tagNET_VCA_DEV_ABILITY = struct_tagNET_VCA_DEV_ABILITY
