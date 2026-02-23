from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_VIOLATION_DETECT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_VIOLATION_DETECT_PARAM, [
    ('dwVioDetectType', DWORD),
    ('byDriveLineSnapTimes', BYTE),
    ('byReverseSnapTimes', BYTE),
    ('wStayTime', WORD),
    ('byNonDriveSnapTimes', BYTE),
    ('byChangeLaneTimes', BYTE),
    ('bybanTimes', BYTE),
    ('byDriveLineSnapSen', BYTE),
    ('wSnapPosFixPixel', WORD),
    ('bySpeedTimes', BYTE),
    ('byTurnAroundEnable', BYTE),
    ('byThirdPlateRecogTime', BYTE),
    ('byPostSnapTimes', BYTE),
    ('byRes1', BYTE * 18),
    ('wStopLineDis', WORD),
    ('byRes', BYTE * 14),
])

NET_ITC_VIOLATION_DETECT_PARAM = struct_tagNET_ITC_VIOLATION_DETECT_PARAM
LPNET_ITC_VIOLATION_DETECT_PARAM = POINTER(struct_tagNET_ITC_VIOLATION_DETECT_PARAM)
tagNET_ITC_VIOLATION_DETECT_PARAM = struct_tagNET_ITC_VIOLATION_DETECT_PARAM
