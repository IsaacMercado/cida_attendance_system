from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_FACE_AND_TEMPLATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FACE_AND_TEMPLATE_CFG, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFaceLen', DWORD),
    ('pFaceBuffer', String),
    ('dwFaceTemplateLen', DWORD),
    ('pFaceTemplateBuffer', String),
    ('byRes', BYTE * 116),
])

NET_DVR_FACE_AND_TEMPLATE_CFG = struct_tagNET_DVR_FACE_AND_TEMPLATE_CFG
LPNET_DVR_FACE_AND_TEMPLATE_CFG = POINTER(struct_tagNET_DVR_FACE_AND_TEMPLATE_CFG)
tagNET_DVR_FACE_AND_TEMPLATE_CFG = struct_tagNET_DVR_FACE_AND_TEMPLATE_CFG
