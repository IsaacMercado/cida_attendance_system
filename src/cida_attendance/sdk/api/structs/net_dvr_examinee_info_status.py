from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXAMINEE_INFO_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_EXAMINEE_INFO_STATUS, [
    ('dwSize', DWORD),
    ('byExamineeNo', BYTE * 64),
    ('byExamRoundNo', BYTE * 64),
    ('byStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_EXAMINEE_INFO_STATUS = struct_tagNET_DVR_EXAMINEE_INFO_STATUS
LPNET_DVR_EXAMINEE_INFO_STATUS = POINTER(struct_tagNET_DVR_EXAMINEE_INFO_STATUS)
tagNET_DVR_EXAMINEE_INFO_STATUS = struct_tagNET_DVR_EXAMINEE_INFO_STATUS
