from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_search import NET_DVR_TIME_SEARCH


class struct_tagNET_DVR_THUMBNAILS_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_THUMBNAILS_RESULT, [
    ('byResultDataType', BYTE),
    ('byIFrameType', BYTE),
    ('byRes1', BYTE * 2),
    ('struTime', NET_DVR_TIME_SEARCH),
    ('byRes', BYTE * 252),
    ('dwFileSize', DWORD),
    ('pBuffer', String),
])

NET_DVR_THUMBNAILS_RESULT = struct_tagNET_DVR_THUMBNAILS_RESULT
LPNET_DVR_THUMBNAILS_RESULT = POINTER(struct_tagNET_DVR_THUMBNAILS_RESULT)
tagNET_DVR_THUMBNAILS_RESULT = struct_tagNET_DVR_THUMBNAILS_RESULT
