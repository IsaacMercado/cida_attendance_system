from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_CAPTURE_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_UPLOAD, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('dwChannel', DWORD),
    ('szDevName', c_char * 64),
    ('dwPicLen', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 124),
])

NET_DVR_CAPTURE_UPLOAD = struct_tagNET_DVR_CAPTURE_UPLOAD
LPNET_DVR_CAPTURE_UPLOAD = POINTER(struct_tagNET_DVR_CAPTURE_UPLOAD)
tagNET_DVR_CAPTURE_UPLOAD = struct_tagNET_DVR_CAPTURE_UPLOAD
