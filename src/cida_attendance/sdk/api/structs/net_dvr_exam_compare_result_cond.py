from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_EXAM_COMPARE_RESULT_COND(Structure):
    pass

_S(struct_tagNET_DVR_EXAM_COMPARE_RESULT_COND, [
    ('dwSize', DWORD),
    ('byExamRoundNo', BYTE * 64),
    ('byExamNo', BYTE * 64),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byRes', BYTE * 512),
])

NET_DVR_EXAM_COMPARE_RESULT_COND = struct_tagNET_DVR_EXAM_COMPARE_RESULT_COND
LPNET_DVR_EXAM_COMPARE_RESULT_COND = POINTER(struct_tagNET_DVR_EXAM_COMPARE_RESULT_COND)
tagNET_DVR_EXAM_COMPARE_RESULT_COND = struct_tagNET_DVR_EXAM_COMPARE_RESULT_COND
