from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXAMINEE_INFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EXAMINEE_INFO_CFG, [
    ('dwSize', DWORD),
    ('byExamineeNo', BYTE * 64),
    ('byAdmissionTicket', BYTE * 64),
    ('byExamRoundNo', BYTE * 64),
    ('byName', BYTE * 32),
    ('byCardNo', BYTE * 32),
    ('bySex', BYTE),
    ('byExamineeInfoValid', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_EXAMINEE_INFO_CFG = struct_tagNET_DVR_EXAMINEE_INFO_CFG
LPNET_DVR_EXAMINEE_INFO_CFG = POINTER(struct_tagNET_DVR_EXAMINEE_INFO_CFG)
tagNET_DVR_EXAMINEE_INFO_CFG = struct_tagNET_DVR_EXAMINEE_INFO_CFG
