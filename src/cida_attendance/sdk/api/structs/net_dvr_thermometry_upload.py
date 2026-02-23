from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_linepolygon_therm_cfg import NET_DVR_LINEPOLYGON_THERM_CFG
from .net_dvr_point_therm_cfg import NET_DVR_POINT_THERM_CFG
from .net_vca_point import NET_VCA_POINT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_THERMOMETRY_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_UPLOAD, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('szRuleName', c_char * 32),
    ('byRuleID', BYTE),
    ('byRuleCalibType', BYTE),
    ('wPresetNo', WORD),
    ('struPointThermCfg', NET_DVR_POINT_THERM_CFG),
    ('struLinePolygonThermCfg', NET_DVR_LINEPOLYGON_THERM_CFG),
    ('byThermometryUnit', BYTE),
    ('byDataType', BYTE),
    ('byRes1', BYTE),
    ('bySpecialPointThermType', BYTE),
    ('fCenterPointTemperature', c_float),
    ('fHighestPointTemperature', c_float),
    ('fLowestPointTemperature', c_float),
    ('struHighestPoint', NET_VCA_POINT),
    ('struLowestPoint', NET_VCA_POINT),
    ('byIsFreezedata', BYTE),
    ('byFaceSnapThermometryEnabled', BYTE),
    ('byRes2', BYTE * 2),
    ('dwChan', DWORD),
    ('struFaceRect', NET_VCA_RECT),
    ('dwTimestamp', DWORD),
    ('byRes', BYTE * 68),
])

NET_DVR_THERMOMETRY_UPLOAD = struct_tagNET_DVR_THERMOMETRY_UPLOAD
LPNET_DVR_THERMOMETRY_UPLOAD = POINTER(struct_tagNET_DVR_THERMOMETRY_UPLOAD)
tagNET_DVR_THERMOMETRY_UPLOAD = struct_tagNET_DVR_THERMOMETRY_UPLOAD
