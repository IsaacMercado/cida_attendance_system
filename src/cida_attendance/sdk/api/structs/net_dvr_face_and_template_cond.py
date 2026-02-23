from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_AND_TEMPLATE_COND(Structure):
    pass

_S(struct_tagNET_DVR_FACE_AND_TEMPLATE_COND, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFaceNum', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_FACE_AND_TEMPLATE_COND = struct_tagNET_DVR_FACE_AND_TEMPLATE_COND
LPNET_DVR_FACE_AND_TEMPLATE_COND = POINTER(struct_tagNET_DVR_FACE_AND_TEMPLATE_COND)
tagNET_DVR_FACE_AND_TEMPLATE_COND = struct_tagNET_DVR_FACE_AND_TEMPLATE_COND
