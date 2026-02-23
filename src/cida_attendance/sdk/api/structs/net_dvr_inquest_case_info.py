from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_CASE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_CASE_INFO, [
    ('dwSize', DWORD),
    ('sCaseNo', BYTE * 64),
    ('sCaseName', BYTE * 64),
    ('sCustomInfo1', BYTE * 64),
    ('sCustomInfo2', BYTE * 64),
    ('sCustomInfo3', BYTE * 64),
    ('byShowCaseInfoTime', BYTE),
    ('byShowCaseInfo', BYTE),
    ('byPosition', BYTE),
    ('byRes1', BYTE),
    ('byCustomInfo4', BYTE * 64),
    ('byCustomInfo5', BYTE * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_INQUEST_CASE_INFO = struct_tagNET_DVR_INQUEST_CASE_INFO
LPNET_DVR_INQUEST_CASE_INFO = POINTER(struct_tagNET_DVR_INQUEST_CASE_INFO)
tagNET_DVR_INQUEST_CASE_INFO = struct_tagNET_DVR_INQUEST_CASE_INFO
