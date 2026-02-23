from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_attendance_time import NET_DVR_ATTENDANCE_TIME


class struct_tagNET_DVR_ABNORMAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ABNORMAL_CFG, [
    ('dwSize', DWORD),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('byDepartmentName', BYTE * 32),
    ('struAttendanceTime', NET_DVR_ATTENDANCE_TIME * 4),
    ('dwLateMinutes', DWORD),
    ('dwLeaveEarlyMinutes', DWORD),
    ('dwAbsenceMinutes', DWORD),
    ('dwTotalMinutes', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ABNORMAL_CFG = struct_tagNET_DVR_ABNORMAL_CFG
LPNET_DVR_ABNORMAL_CFG = POINTER(struct_tagNET_DVR_ABNORMAL_CFG)
tagNET_DVR_ABNORMAL_CFG = struct_tagNET_DVR_ABNORMAL_CFG
