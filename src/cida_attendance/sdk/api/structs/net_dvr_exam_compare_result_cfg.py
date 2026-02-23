from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_EXAM_COMPARE_RESULT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EXAM_COMPARE_RESULT_CFG, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME),
    ('byExamineeNo', BYTE * 64),
    ('byAdmissionTicket', BYTE * 64),
    ('byExamNo', BYTE * 64),
    ('byExamRoundNo', BYTE * 64),
    ('byName', BYTE * 32),
    ('byCardNo', BYTE * 32),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('byRes', BYTE * 256),
])

NET_DVR_EXAM_COMPARE_RESULT_CFG = struct_tagNET_DVR_EXAM_COMPARE_RESULT_CFG
LPNET_DVR_EXAM_COMPARE_RESULT_CFG = POINTER(struct_tagNET_DVR_EXAM_COMPARE_RESULT_CFG)
tagNET_DVR_EXAM_COMPARE_RESULT_CFG = struct_tagNET_DVR_EXAM_COMPARE_RESULT_CFG
