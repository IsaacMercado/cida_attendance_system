from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..functions import DATADOWNLOAD


class struct_tagNET_DVR_DOWNLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_PARAM, [
    ('dwSize', DWORD),
    ('byDownType', BYTE),
    ('byDataType', BYTE),
    ('byDataNum', BYTE),
    ('byRes1', BYTE),
    ('sFileName', c_char * 260),
    ('lpDataCallBack', DATADOWNLOAD),
    ('pUserData', POINTER(None)),
    ('byRes2', BYTE * 128),
])

NET_DVR_DOWNLOAD_PARAM = struct_tagNET_DVR_DOWNLOAD_PARAM
LPNET_DVR_DOWNLOAD_PARAM = POINTER(struct_tagNET_DVR_DOWNLOAD_PARAM)
tagNET_DVR_DOWNLOAD_PARAM = struct_tagNET_DVR_DOWNLOAD_PARAM
