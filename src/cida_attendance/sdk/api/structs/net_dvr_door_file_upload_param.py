from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DOOR_FILE_UPLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DOOR_FILE_UPLOAD_PARAM, [
    ('dwSize', DWORD),
    ('dwFileSize', DWORD),
    ('byFileName', BYTE * 100),
    ('byRes1', BYTE * 256),
])

NET_DVR_DOOR_FILE_UPLOAD_PARAM = struct_tagNET_DVR_DOOR_FILE_UPLOAD_PARAM
LPNET_DVR_DOOR_FILE_UPLOAD_PARAM = POINTER(struct_tagNET_DVR_DOOR_FILE_UPLOAD_PARAM)
tagNET_DVR_DOOR_FILE_UPLOAD_PARAM = struct_tagNET_DVR_DOOR_FILE_UPLOAD_PARAM
