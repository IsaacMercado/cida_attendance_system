from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_FACECAPTURE_STATISTICS_COND(Structure):
    pass

_S(struct_tagNET_DVR_FACECAPTURE_STATISTICS_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('byReportType', BYTE),
    ('byStatType', BYTE),
    ('byEnableProgramStatistics', BYTE),
    ('byRes1', BYTE),
    ('dwPlayScheduleNo', DWORD),
    ('byRes', BYTE * 120),
])

NET_DVR_FACECAPTURE_STATISTICS_COND = struct_tagNET_DVR_FACECAPTURE_STATISTICS_COND
LPNET_DVR_FACECAPTURE_STATISTICS_COND = POINTER(struct_tagNET_DVR_FACECAPTURE_STATISTICS_COND)
tagNET_DVR_FACECAPTURE_STATISTICS_COND = struct_tagNET_DVR_FACECAPTURE_STATISTICS_COND
