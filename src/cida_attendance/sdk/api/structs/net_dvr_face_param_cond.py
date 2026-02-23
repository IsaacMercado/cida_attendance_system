from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_PARAM_COND(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PARAM_COND, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('dwFaceNum', DWORD),
    ('byFaceID', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_FACE_PARAM_COND = struct_tagNET_DVR_FACE_PARAM_COND
LPNET_DVR_FACE_PARAM_COND = POINTER(struct_tagNET_DVR_FACE_PARAM_COND)
tagNET_DVR_FACE_PARAM_COND = struct_tagNET_DVR_FACE_PARAM_COND
