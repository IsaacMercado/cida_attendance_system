from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_COURSE_RECORDING_INFO(Structure):
    pass

_S(struct_tagNET_DVR_COURSE_RECORDING_INFO, [
    ('dwSize', DWORD),
    ('sCourseName', c_char * 32),
    ('sInstructorName', c_char * 16),
    ('sCourseDescription', c_char * 256),
    ('byIndex', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_COURSE_RECORDING_INFO = struct_tagNET_DVR_COURSE_RECORDING_INFO
LPNET_DVR_COURSE_RECORDING_INFO = POINTER(struct_tagNET_DVR_COURSE_RECORDING_INFO)
tagNET_DVR_COURSE_RECORDING_INFO = struct_tagNET_DVR_COURSE_RECORDING_INFO
