from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_THERMOMETRY_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_FACE_THERMOMETRY_ALARM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRuleID', BYTE),
    ('byRes1', BYTE * 3),
    ('byRuleName', BYTE * 32),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byFaceDetectionState', BYTE),
    ('byThermometryUnit', BYTE),
    ('byAlarmRule', BYTE),
    ('byRes2', BYTE * 1),
    ('fAlarmTemperature', c_float),
    ('fRuleTemperature', c_float),
    ('dwVisibleLightImageLen', DWORD),
    ('pVisibleLightImage', POINTER(BYTE)),
    ('dwFaceImageLen', DWORD),
    ('pFaceImage', POINTER(BYTE)),
    ('struFaceRegion', NET_VCA_RECT),
    ('fMinTemperature', c_float),
    ('fAverageTemperature', c_float),
    ('struMinTemperaturePoint', NET_VCA_POINT),
    ('struMaxTemperaturePoint', NET_VCA_POINT),
    ('byRes', BYTE * 720),
])

NET_DVR_FACE_THERMOMETRY_ALARM = struct_tagNET_DVR_FACE_THERMOMETRY_ALARM
LPNET_DVR_FACE_THERMOMETRY_ALARM = POINTER(struct_tagNET_DVR_FACE_THERMOMETRY_ALARM)
tagNET_DVR_FACE_THERMOMETRY_ALARM = struct_tagNET_DVR_FACE_THERMOMETRY_ALARM
