from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_FACE_PARAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PARAM_CFG, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFaceLen', DWORD),
    ('pFaceBuffer', String),
    ('byEnableCardReader', BYTE * 512),
    ('byFaceID', BYTE),
    ('byFaceDataType', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_FACE_PARAM_CFG = struct_tagNET_DVR_FACE_PARAM_CFG
LPNET_DVR_FACE_PARAM_CFG = POINTER(struct_tagNET_DVR_FACE_PARAM_CFG)
tagNET_DVR_FACE_PARAM_CFG = struct_tagNET_DVR_FACE_PARAM_CFG
