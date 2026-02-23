from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAPTURE_FACE_COND(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_FACE_COND, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_CAPTURE_FACE_COND = struct_tagNET_DVR_CAPTURE_FACE_COND
LPNET_DVR_CAPTURE_FACE_COND = POINTER(struct_tagNET_DVR_CAPTURE_FACE_COND)
tagNET_DVR_CAPTURE_FACE_COND = struct_tagNET_DVR_CAPTURE_FACE_COND
