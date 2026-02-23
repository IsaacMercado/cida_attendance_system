from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_FACE_STATUS(Structure):
    pass

_S(struct__NET_DVR_FACE_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byErrorMsg', BYTE * 32),
    ('dwReaderNo', DWORD),
    ('byRecvStatus', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_FACE_STATUS = struct__NET_DVR_FACE_STATUS
LPNET_DVR_FACE_STATUS = POINTER(struct__NET_DVR_FACE_STATUS)
_NET_DVR_FACE_STATUS = struct__NET_DVR_FACE_STATUS
