from ctypes import Structure

from ..base_classes import _S, BYTE, INT64
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_DB_IN(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_DB_IN, [
    ('i64FileLen', INT64),
    ('byContinueUpload', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_UPLOAD_DB_IN = struct_tagNET_DVR_UPLOAD_DB_IN
LPNET_DVR_UPLOAD_DB_IN = POINTER(struct_tagNET_DVR_UPLOAD_DB_IN)
tagNET_DVR_UPLOAD_DB_IN = struct_tagNET_DVR_UPLOAD_DB_IN
