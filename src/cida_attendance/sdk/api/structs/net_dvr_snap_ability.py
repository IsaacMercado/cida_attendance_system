from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNAP_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_SNAP_ABILITY, [
    ('dwSize', DWORD),
    ('byIoInNum', BYTE),
    ('byIoOutNum', BYTE),
    ('bySingleSnapNum', BYTE),
    ('byLightModeArrayNum', BYTE),
    ('byMeasureModeArrayNum', BYTE),
    ('byPlateEnable', BYTE),
    ('byLensMode', BYTE),
    ('byPreTriggerSupport', BYTE),
    ('dwAbilityType', DWORD),
    ('byIoSpeedGroup', BYTE),
    ('byIoLightGroup', BYTE),
    ('byRecogRegionType', BYTE),
    ('bySupport', BYTE),
    ('wSupportMultiRadar', WORD),
    ('byICRPresetNum', BYTE),
    ('byICRTimeSlot', BYTE),
    ('bySupportRS485Num', BYTE),
    ('byExpandRs485SupportSensor', BYTE),
    ('byExpandRs485SupportSignalLampDet', BYTE),
    ('byRelayNum', BYTE),
    ('bySupport1', BYTE),
    ('bySupport2', BYTE),
    ('bySupportWhiteBalance', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_SNAP_ABILITY = struct_tagNET_DVR_SNAP_ABILITY
LPNET_DVR_SNAP_ABILITY = POINTER(struct_tagNET_DVR_SNAP_ABILITY)
tagNET_DVR_SNAP_ABILITY = struct_tagNET_DVR_SNAP_ABILITY
