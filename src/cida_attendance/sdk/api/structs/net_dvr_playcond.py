from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_PLAYCOND(Structure):
    pass

_S(struct_tagNET_DVR_PLAYCOND, [
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byDrawFrame', BYTE),
    ('byStreamType', BYTE),
    ('byStreamID', BYTE * 32),
    ('byCourseFile', BYTE),
    ('byDownload', BYTE),
    ('byOptimalStreamType', BYTE),
    ('byVODFileType', BYTE),
    ('byRes', BYTE * 26),
])

NET_DVR_PLAYCOND = struct_tagNET_DVR_PLAYCOND
LPNET_DVR_PLAYCOND = POINTER(struct_tagNET_DVR_PLAYCOND)
tagNET_DVR_PLAYCOND = struct_tagNET_DVR_PLAYCOND
