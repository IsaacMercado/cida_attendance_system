from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_NET_DVR_UPLOAD_FACE_DATA_OUT(Structure):
    pass

_S(struct_NET_DVR_UPLOAD_FACE_DATA_OUT, [
    ('szPicID', c_char * 256),
    ('byRes', BYTE * 128),
])

NET_DVR_UPLOAD_FACE_DATA_OUT = struct_NET_DVR_UPLOAD_FACE_DATA_OUT
LPNET_DVR_UPLOAD_FACE_DATA_OUT = POINTER(struct_NET_DVR_UPLOAD_FACE_DATA_OUT)
NET_DVR_UPLOAD_FACE_DATA_OUT = struct_NET_DVR_UPLOAD_FACE_DATA_OUT
