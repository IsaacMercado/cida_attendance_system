from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MOBILE_RADAR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MOBILE_RADAR_CFG, [
    ('dwSize', DWORD),
    ('byEnableRadar', BYTE),
    ('byEnableAlarm', BYTE),
    ('wOverSpeed', WORD),
    ('bySpeedUnits', BYTE),
    ('bydirection', BYTE),
    ('byMeasureMode', BYTE),
    ('byTargetType', BYTE),
    ('bySensitivity', BYTE),
    ('byCaptureNum', BYTE),
    ('byUploadPlate', BYTE),
    ('byRes', BYTE * 61),
])

NET_DVR_MOBILE_RADAR_CFG = struct_tagNET_DVR_MOBILE_RADAR_CFG
LPNET_DVR_MOBILE_RADAR_CFG = POINTER(struct_tagNET_DVR_MOBILE_RADAR_CFG)
tagNET_DVR_MOBILE_RADAR_CFG = struct_tagNET_DVR_MOBILE_RADAR_CFG
