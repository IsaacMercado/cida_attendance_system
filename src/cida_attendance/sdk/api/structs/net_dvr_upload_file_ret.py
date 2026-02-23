from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_FILE_RET(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_FILE_RET, [
    ('sUrl', BYTE * 240),
    ('byRes', BYTE * 260),
])

NET_DVR_UPLOAD_FILE_RET = struct_tagNET_DVR_UPLOAD_FILE_RET
LPNET_DVR_UPLOAD_FILE_RET = POINTER(struct_tagNET_DVR_UPLOAD_FILE_RET)
tagNET_DVR_UPLOAD_FILE_RET = struct_tagNET_DVR_UPLOAD_FILE_RET
