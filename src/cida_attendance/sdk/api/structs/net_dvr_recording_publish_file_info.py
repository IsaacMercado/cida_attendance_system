from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_RECORDING_PUBLISH_FILE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_INFO, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byCourseName', BYTE * 128),
    ('byInstructorName', BYTE * 64),
    ('byCourseDescription', BYTE * 256),
    ('byRes', BYTE * 300),
])

NET_DVR_RECORDING_PUBLISH_FILE_INFO = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_INFO
LPNET_DVR_RECORDING_PUBLISH_FILE_INFO = POINTER(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_INFO)
tagNET_DVR_RECORDING_PUBLISH_FILE_INFO = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_INFO
