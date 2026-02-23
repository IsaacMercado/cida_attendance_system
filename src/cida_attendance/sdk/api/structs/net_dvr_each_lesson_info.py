from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_EACH_LESSON_INFO_(Structure):
    pass

_S(struct_tagNET_DVR_EACH_LESSON_INFO_, [
    ('struSchedTime', NET_DVR_SCHEDTIME),
    ('wCourseIndex', WORD),
    ('wSessionIndex', WORD),
    ('byRes', BYTE * 4),
])

NET_DVR_EACH_LESSON_INFO = struct_tagNET_DVR_EACH_LESSON_INFO_
LPNET_DVR_EACH_LESSON_INFO = POINTER(struct_tagNET_DVR_EACH_LESSON_INFO_)
tagNET_DVR_EACH_LESSON_INFO_ = struct_tagNET_DVR_EACH_LESSON_INFO_
