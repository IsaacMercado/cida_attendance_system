from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ATTENDANCE_SUMMARY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ATTENDANCE_SUMMARY_CFG, [
    ('dwSize', DWORD),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('byDepartmentName', BYTE * 32),
    ('dwWorkStandard', DWORD),
    ('dwWorkActual', DWORD),
    ('dwLateTimes', DWORD),
    ('dwLateMinutes', DWORD),
    ('dwLeaveEarlyTimes', DWORD),
    ('dwLeaveEarlyMinutes', DWORD),
    ('dwOvertimeStandard', DWORD),
    ('dwOvertimeActual', DWORD),
    ('dwAttendanceStandard', DWORD),
    ('dwAttendanceActual', DWORD),
    ('dwAbsentDays', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ATTENDANCE_SUMMARY_CFG = struct_tagNET_DVR_ATTENDANCE_SUMMARY_CFG
LPNET_DVR_ATTENDANCE_SUMMARY_CFG = POINTER(struct_tagNET_DVR_ATTENDANCE_SUMMARY_CFG)
tagNET_DVR_ATTENDANCE_SUMMARY_CFG = struct_tagNET_DVR_ATTENDANCE_SUMMARY_CFG
