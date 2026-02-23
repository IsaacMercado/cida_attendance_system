from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_COURSE_LIST_COND(Structure):
    pass

_S(struct_tagNET_DVR_COURSE_LIST_COND, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byCourseName', BYTE * 128),
    ('byInstructorName', BYTE * 64),
    ('byCourseType', BYTE),
    ('byRes', BYTE * 603),
])

NET_DVR_COURSE_LIST_COND = struct_tagNET_DVR_COURSE_LIST_COND
LPNET_DVR_COURSE_LIST_COND = POINTER(struct_tagNET_DVR_COURSE_LIST_COND)
tagNET_DVR_COURSE_LIST_COND = struct_tagNET_DVR_COURSE_LIST_COND
