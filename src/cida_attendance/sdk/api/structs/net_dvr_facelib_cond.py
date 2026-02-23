from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACELIB_COND(Structure):
    pass

_S(struct_tagNET_DVR_FACELIB_COND, [
    ('dwSize', DWORD),
    ('szFDID', c_char * 256),
    ('byConcurrent', BYTE),
    ('byCover', BYTE),
    ('byCustomFaceLibID', BYTE),
    ('byPictureSaveMode', BYTE),
    ('byIdentityKey', BYTE * 64),
    ('byRes', BYTE * 60),
])

NET_DVR_FACELIB_COND = struct_tagNET_DVR_FACELIB_COND
LPNET_DVR_FACELIB_COND = POINTER(struct_tagNET_DVR_FACELIB_COND)
tagNET_DVR_FACELIB_COND = struct_tagNET_DVR_FACELIB_COND
