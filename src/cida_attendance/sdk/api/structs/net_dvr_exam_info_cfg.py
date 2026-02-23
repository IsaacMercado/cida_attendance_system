from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_EXAM_INFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EXAM_INFO_CFG, [
    ('dwSize', DWORD),
    ('byExamRoundNo', BYTE * 64),
    ('byExamNo', BYTE * 64),
    ('byExamSubject', BYTE * 64),
    ('byTeacherNo', BYTE * 64),
    ('byTeacherName', BYTE * 64),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byExamInfoValid', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_EXAM_INFO_CFG = struct_tagNET_DVR_EXAM_INFO_CFG
LPNET_DVR_EXAM_INFO_CFG = POINTER(struct_tagNET_DVR_EXAM_INFO_CFG)
tagNET_DVR_EXAM_INFO_CFG = struct_tagNET_DVR_EXAM_INFO_CFG
