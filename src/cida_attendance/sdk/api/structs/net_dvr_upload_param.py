from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_UPLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_PARAM, [
    ('dwSize', DWORD),
    ('byUploadType', BYTE),
    ('byDataType', BYTE),
    ('byDataNum', BYTE),
    ('byAudioType', BYTE),
    ('sFileName', c_char * 260),
    ('lpBuffer', String),
    ('dwBufferSize', DWORD),
    ('byRes2', BYTE * 128),
])

NET_DVR_UPLOAD_PARAM = struct_tagNET_DVR_UPLOAD_PARAM
LPNET_DVR_UPLOAD_PARAM = POINTER(struct_tagNET_DVR_UPLOAD_PARAM)
tagNET_DVR_UPLOAD_PARAM = struct_tagNET_DVR_UPLOAD_PARAM
