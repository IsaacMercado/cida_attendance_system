from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_COURSE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_COURSE_CFG, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byCourseName', BYTE * 128),
    ('byInstructorName', BYTE * 64),
    ('byCourseDescription', BYTE * 256),
    ('byRecUUID', BYTE * 64),
    ('byCourseType', BYTE),
    ('byRes', BYTE * 303),
])

NET_DVR_COURSE_CFG = struct_tagNET_DVR_COURSE_CFG
LPNET_DVR_COURSE_CFG = POINTER(struct_tagNET_DVR_COURSE_CFG)
tagNET_DVR_COURSE_CFG = struct_tagNET_DVR_COURSE_CFG
