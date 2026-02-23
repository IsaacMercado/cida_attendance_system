from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_FACE_COND(Structure):
    pass

_S(struct__NET_DVR_FACE_COND, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFaceNum', DWORD),
    ('dwEnableReaderNo', DWORD),
    ('byRes', BYTE * 124),
])

NET_DVR_FACE_COND = struct__NET_DVR_FACE_COND
LPNET_DVR_FACE_COND = POINTER(struct__NET_DVR_FACE_COND)
_NET_DVR_FACE_COND = struct__NET_DVR_FACE_COND
