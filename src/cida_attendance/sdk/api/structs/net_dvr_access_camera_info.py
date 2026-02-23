from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACCESS_CAMERA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACCESS_CAMERA_INFO, [
    ('dwSize', DWORD),
    ('sCameraInfo', c_char * 32),
    ('byInterfaceType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_ACCESS_CAMERA_INFO = struct_tagNET_DVR_ACCESS_CAMERA_INFO
LPNET_DVR_ACCESS_CAMERA_INFO = POINTER(struct_tagNET_DVR_ACCESS_CAMERA_INFO)
tagNET_DVR_ACCESS_CAMERA_INFO = struct_tagNET_DVR_ACCESS_CAMERA_INFO
