from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_FACE_RECORD(Structure):
    pass

_S(struct__NET_DVR_FACE_RECORD, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFaceLen', DWORD),
    ('pFaceBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 128),
])

NET_DVR_FACE_RECORD = struct__NET_DVR_FACE_RECORD
LPNET_DVR_FACE_RECORD = POINTER(struct__NET_DVR_FACE_RECORD)
_NET_DVR_FACE_RECORD = struct__NET_DVR_FACE_RECORD
