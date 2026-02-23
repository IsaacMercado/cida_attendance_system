from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_dvr_pdc_enter_direction import NET_DVR_PDC_ENTER_DIRECTION
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_line import NET_VCA_LINE
from .net_vca_point import NET_VCA_POINT
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_polyline import NET_VCA_POLYLINE


class struct_tagNET_DVR_PDC_RULE_CFG_V42(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RULE_CFG_V42, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byOSDEnable', BYTE),
    ('byCurDetectType', BYTE),
    ('byInterferenceSuppression', BYTE),
    ('struOSDPoint', NET_VCA_POINT),
    ('byDataUploadCycle', BYTE),
    ('bySECUploadEnable', BYTE),
    ('byEmailDayReport', BYTE),
    ('byEmailWeekReport', BYTE),
    ('byEmailMonthReport', BYTE),
    ('byEmailYearReport', BYTE),
    ('byRes2', BYTE * 6),
    ('struPolygon', NET_VCA_POLYGON),
    ('struEnterDirection', NET_DVR_PDC_ENTER_DIRECTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struDayStartTime', NET_DVR_TIME_EX),
    ('struNightStartTime', NET_DVR_TIME_EX),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V40),
    ('byDetecteSensitivity', BYTE),
    ('byGenerateSpeedSpace', BYTE),
    ('byGenerateSpeedTime', BYTE),
    ('byCountSpeed', BYTE),
    ('byDetecteType', BYTE),
    ('byTargetSizeCorrect', BYTE),
    ('byStreamOverlayRuleInfos', BYTE),
    ('byRes3', BYTE),
    ('struLine', NET_VCA_LINE),
    ('byHeightFilterEnable', BYTE),
    ('byDetectThreshold', BYTE),
    ('byAidedTrackEnabled', BYTE),
    ('byRes4', BYTE),
    ('fHeightFilter', c_float),
    ('byCalibrateType', BYTE),
    ('byCountingType', BYTE),
    ('bySignalType', BYTE),
    ('byRS485TransmissionEnabled', BYTE),
    ('fTiltAngle', c_float),
    ('fHeelAngle', c_float),
    ('fHeight', c_float),
    ('struCountPolygon', NET_VCA_POLYGON),
    ('struAutoCalibPolygon', NET_VCA_POLYGON),
    ('struDailyResetTime', NET_DVR_TIME_EX),
    ('struPolyLine', NET_VCA_POLYLINE),
    ('byRes', BYTE * 4),
])

NET_DVR_PDC_RULE_CFG_V42 = struct_tagNET_DVR_PDC_RULE_CFG_V42
LPNET_DVR_PDC_RULE_CFG_V42 = POINTER(struct_tagNET_DVR_PDC_RULE_CFG_V42)
tagNET_DVR_PDC_RULE_CFG_V42 = struct_tagNET_DVR_PDC_RULE_CFG_V42
