from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FAILED_FACE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FAILED_FACE_INFO, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byErrorCode', BYTE),
    ('byRes1', BYTE * 3),
    ('byEmployeeNo', BYTE * 32),
    ('byRes', BYTE * 92),
])

NET_DVR_FAILED_FACE_INFO = struct_tagNET_DVR_FAILED_FACE_INFO
LPNET_DVR_FAILED_FACE_INFO = POINTER(struct_tagNET_DVR_FAILED_FACE_INFO)
tagNET_DVR_FAILED_FACE_INFO = struct_tagNET_DVR_FAILED_FACE_INFO
