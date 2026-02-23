from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, HWND
from ..ctypes_preamble import POINTER, String
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_v50 import NET_DVR_TIME_V50


class struct_tagNET_DVR_VOD_PARA_V50(Structure):
    pass

_S(struct_tagNET_DVR_VOD_PARA_V50, [
    ('dwSize', DWORD),
    ('struIDInfo', NET_DVR_STREAM_INFO),
    ('struBeginTime', NET_DVR_TIME_V50),
    ('struEndTime', NET_DVR_TIME_V50),
    ('hWnd', HWND),
    ('byDrawFrame', BYTE),
    ('byVolumeType', BYTE),
    ('byVolumeNum', BYTE),
    ('byStreamType', BYTE),
    ('dwFileIndex', DWORD),
    ('byAudioFile', BYTE),
    ('byCourseFile', BYTE),
    ('byPlayMode', BYTE),
    ('byLinkMode', BYTE),
    ('byDownload', BYTE),
    ('byOptimalStreamType', BYTE),
    ('byDisplayBufNum', BYTE),
    ('byNPQMode', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRemoteFile', BYTE),
    ('byUseAsyn', BYTE),
    ('byRes2', BYTE * 201),
    ('byHls', BYTE),
    ('pSavedFileName', String),
])

NET_DVR_VOD_PARA_V50 = struct_tagNET_DVR_VOD_PARA_V50
LPNET_DVR_VOD_PARA_V50 = POINTER(struct_tagNET_DVR_VOD_PARA_V50)
tagNET_DVR_VOD_PARA_V50 = struct_tagNET_DVR_VOD_PARA_V50
