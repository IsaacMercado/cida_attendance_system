from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_CHECK_FACE_PICTURE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CHECK_FACE_PICTURE_CFG, [
    ('dwSize', DWORD),
    ('dwPictureNo', DWORD),
    ('dwPictureLen', DWORD),
    ('pPictureBuffer', String),
    ('dwFaceTemplateLen', DWORD),
    ('pFaceTemplateBuffer', String),
    ('byRes', BYTE * 248),
])

NET_DVR_CHECK_FACE_PICTURE_CFG = struct_tagNET_DVR_CHECK_FACE_PICTURE_CFG
LPNET_DVR_CHECK_FACE_PICTURE_CFG = POINTER(struct_tagNET_DVR_CHECK_FACE_PICTURE_CFG)
tagNET_DVR_CHECK_FACE_PICTURE_CFG = struct_tagNET_DVR_CHECK_FACE_PICTURE_CFG
