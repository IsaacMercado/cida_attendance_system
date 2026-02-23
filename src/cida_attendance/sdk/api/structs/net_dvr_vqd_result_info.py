from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_VQD_RESULT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VQD_RESULT_INFO, [
    ('dwSize', DWORD),
    ('sStreamID', c_char * 32),
    ('dwPicLength', DWORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 31),
    ('pSnapShot', String),
])

NET_DVR_VQD_RESULT_INFO = struct_tagNET_DVR_VQD_RESULT_INFO
LPNET_DVR_VQD_RESULT_INFO = POINTER(struct_tagNET_DVR_VQD_RESULT_INFO)
tagNET_DVR_VQD_RESULT_INFO = struct_tagNET_DVR_VQD_RESULT_INFO
