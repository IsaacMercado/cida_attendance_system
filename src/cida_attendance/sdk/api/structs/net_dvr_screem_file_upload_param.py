from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM, [
    ('dwSize', DWORD),
    ('byFileType', BYTE),
    ('byPictureFormat', BYTE),
    ('byVideoFormat', BYTE),
    ('byDocumentFormat', BYTE),
    ('byFileName', BYTE * 256),
    ('byOtherFileFormat', BYTE * 8),
    ('byRes1', BYTE * 56),
])

NET_DVR_SCREEM_FILE_UPLOAD_PARAM = struct_tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM
LPNET_DVR_SCREEM_FILE_UPLOAD_PARAM = POINTER(struct_tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM)
tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM = struct_tagNET_DVR_SCREEM_FILE_UPLOAD_PARAM
