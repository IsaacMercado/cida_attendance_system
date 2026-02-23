from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHECK_FACE_PICTURE_COND(Structure):
    pass

_S(struct_tagNET_DVR_CHECK_FACE_PICTURE_COND, [
    ('dwSize', DWORD),
    ('dwPictureNum', DWORD),
    ('byCheckTemplate', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_CHECK_FACE_PICTURE_COND = struct_tagNET_DVR_CHECK_FACE_PICTURE_COND
LPNET_DVR_CHECK_FACE_PICTURE_COND = POINTER(struct_tagNET_DVR_CHECK_FACE_PICTURE_COND)
tagNET_DVR_CHECK_FACE_PICTURE_COND = struct_tagNET_DVR_CHECK_FACE_PICTURE_COND
