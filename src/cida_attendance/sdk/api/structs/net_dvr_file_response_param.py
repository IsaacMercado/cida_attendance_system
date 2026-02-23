from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FILE_RESPONSE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FILE_RESPONSE_PARAM, [
    ('byFileState', BYTE),
    ('byRes1', BYTE * 3),
    ('dwErrorFileIndex', DWORD),
    ('byRes2', BYTE * 24),
])

NET_DVR_FILE_RESPONSE_PARAM = struct_tagNET_DVR_FILE_RESPONSE_PARAM
LPNET_DVR_FILE_RESPONSE_PARAM = POINTER(struct_tagNET_DVR_FILE_RESPONSE_PARAM)
tagNET_DVR_FILE_RESPONSE_PARAM = struct_tagNET_DVR_FILE_RESPONSE_PARAM
