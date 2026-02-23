from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_PLATE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_PLATE_INFO, [
    ('sLicense', c_char * 16),
    ('byColor', BYTE),
    ('byRes', BYTE * 239),
])

NET_DVR_UPLOAD_PLATE_INFO = struct_tagNET_DVR_UPLOAD_PLATE_INFO
LPNET_DVR_UPLOAD_PLATE_INFO = POINTER(struct_tagNET_DVR_UPLOAD_PLATE_INFO)
tagNET_DVR_UPLOAD_PLATE_INFO = struct_tagNET_DVR_UPLOAD_PLATE_INFO
