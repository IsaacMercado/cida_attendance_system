from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_UPLOAD_FACE_DATA(Structure):
    pass

_S(struct_NET_DVR_UPLOAD_FACE_DATA, [
    ('dwSize', DWORD),
    ('szFDID', c_char * 256),
    ('byFDLibType', BYTE),
    ('byRes1', BYTE * 3),
    ('szCustomInfo', c_char * 96),
    ('byRes', BYTE * 512),
])

NET_DVR_UPLOAD_FACE_DATA = struct_NET_DVR_UPLOAD_FACE_DATA
LPNET_DVR_UPLOAD_FACE_DATA = POINTER(struct_NET_DVR_UPLOAD_FACE_DATA)
NET_DVR_UPLOAD_FACE_DATA = struct_NET_DVR_UPLOAD_FACE_DATA
