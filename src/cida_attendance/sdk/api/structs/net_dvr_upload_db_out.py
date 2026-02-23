from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_DB_OUT(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_DB_OUT, [
    ('szFileID', c_char * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_UPLOAD_DB_OUT = struct_tagNET_DVR_UPLOAD_DB_OUT
LPNET_DVR_UPLOAD_DB_OUT = POINTER(struct_tagNET_DVR_UPLOAD_DB_OUT)
tagNET_DVR_UPLOAD_DB_OUT = struct_tagNET_DVR_UPLOAD_DB_OUT
