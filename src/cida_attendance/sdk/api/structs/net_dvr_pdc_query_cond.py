from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_PDC_QUERY_COND(Structure):
    pass

_S(struct_tagNET_DVR_PDC_QUERY_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byReportType', BYTE),
    ('byEnableProgramStatistics', BYTE),
    ('byTriggerPeopleCountingData', BYTE),
    ('byMultiChannelSearch', BYTE),
    ('dwPlayScheduleNo', DWORD),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes1', BYTE * 3),
    ('dwSearchChannelNum', DWORD),
    ('pSearchChannel', String),
    ('byChild', BYTE),
    ('byMinTimeInterva', BYTE),
    ('byStatisticType', BYTE),
    ('byFaceExpression', BYTE),
    ('byGender', BYTE),
    ('byMask', BYTE),
    ('byAgeGroup', BYTE),
    ('byGlasses', BYTE),
    ('byRes', BYTE * 96),
])

NET_DVR_PDC_QUERY_COND = struct_tagNET_DVR_PDC_QUERY_COND
LPNET_DVR_PDC_QUERY_COND = POINTER(struct_tagNET_DVR_PDC_QUERY_COND)
tagNET_DVR_PDC_QUERY_COND = struct_tagNET_DVR_PDC_QUERY_COND
