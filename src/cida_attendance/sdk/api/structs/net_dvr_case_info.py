from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CASE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CASE_INFO, [
    ('dwSize', DWORD),
    ('byCaseNo', BYTE * 64),
    ('byCaseName', BYTE * 128),
    ('byLitigant1', BYTE * 32),
    ('byLitigant2', BYTE * 32),
    ('byChiefJudge', BYTE * 32),
    ('byCaseType', BYTE),
    ('byShowCaseInfoTime', BYTE),
    ('byRes1', BYTE * 2),
    ('sCaseTypeCustom', c_char * 32),
    ('byRes', BYTE * 220),
])

NET_DVR_CASE_INFO = struct_tagNET_DVR_CASE_INFO
LPNET_DVR_CASE_INFO = POINTER(struct_tagNET_DVR_CASE_INFO)
tagNET_DVR_CASE_INFO = struct_tagNET_DVR_CASE_INFO
