from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXAMINEE_INFO_COND(Structure):
    pass

_S(struct_tagNET_DVR_EXAMINEE_INFO_COND, [
    ('dwSize', DWORD),
    ('dwExamineeNumber', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_EXAMINEE_INFO_COND = struct_tagNET_DVR_EXAMINEE_INFO_COND
LPNET_DVR_EXAMINEE_INFO_COND = POINTER(struct_tagNET_DVR_EXAMINEE_INFO_COND)
tagNET_DVR_EXAMINEE_INFO_COND = struct_tagNET_DVR_EXAMINEE_INFO_COND
