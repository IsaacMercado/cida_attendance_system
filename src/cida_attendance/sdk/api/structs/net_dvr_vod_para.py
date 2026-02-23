from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, HWND
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_VOD_PARA(Structure):
    pass

_S(struct_tagNET_DVR_VOD_PARA, [
    ('dwSize', DWORD),
    ('struIDInfo', NET_DVR_STREAM_INFO),
    ('struBeginTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('hWnd', HWND),
    ('byDrawFrame', BYTE),
    ('byVolumeType', BYTE),
    ('byVolumeNum', BYTE),
    ('byStreamType', BYTE),
    ('dwFileIndex', DWORD),
    ('byAudioFile', BYTE),
    ('byCourseFile', BYTE),
    ('byDownload', BYTE),
    ('byOptimalStreamType', BYTE),
    ('byUseAsyn', BYTE),
    ('byRes2', BYTE * 19),
])

NET_DVR_VOD_PARA = struct_tagNET_DVR_VOD_PARA
LPNET_DVR_VOD_PARA = POINTER(struct_tagNET_DVR_VOD_PARA)
tagNET_DVR_VOD_PARA = struct_tagNET_DVR_VOD_PARA
