from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_UPLOAD_PICTURE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_PICTURE_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byPictureType', BYTE),
    ('byRes1', BYTE * 3),
    ('struTime', NET_DVR_TIME_V30),
    ('sPictureBuffer', String),
    ('dwPictureLength', DWORD),
    ('dwPicMangeNo', DWORD),
    ('sPicName', BYTE * 32),
    ('byUseType', BYTE),
    ('byRes', BYTE * 91),
])

NET_DVR_UPLOAD_PICTURE_INFO = struct_tagNET_DVR_UPLOAD_PICTURE_INFO
LPNET_DVR_UPLOAD_PICTURE_INFO = POINTER(struct_tagNET_DVR_UPLOAD_PICTURE_INFO)
tagNET_DVR_UPLOAD_PICTURE_INFO = struct_tagNET_DVR_UPLOAD_PICTURE_INFO
