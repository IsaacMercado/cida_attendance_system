from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_ATTENDANCE_RECORD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ATTENDANCE_RECORD_CFG, [
    ('dwSize', DWORD),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('byDepartmentName', BYTE * 32),
    ('struAttendanceTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 128),
])

NET_DVR_ATTENDANCE_RECORD_CFG = struct_tagNET_DVR_ATTENDANCE_RECORD_CFG
LPNET_DVR_ATTENDANCE_RECORD_CFG = POINTER(struct_tagNET_DVR_ATTENDANCE_RECORD_CFG)
tagNET_DVR_ATTENDANCE_RECORD_CFG = struct_tagNET_DVR_ATTENDANCE_RECORD_CFG
