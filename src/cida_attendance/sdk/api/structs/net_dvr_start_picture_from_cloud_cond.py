from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..functions import DOWNLOAD_DATA_CB
from .anon_458 import union_anon_458
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_COND(Structure):
    pass

_S(struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_COND, [
    ('dwSize', DWORD),
    ('aCameraID', BYTE * 64),
    ('struBeginTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('dwPicType', DWORD),
    ('byRes1', BYTE * 3),
    ('byZoomType', BYTE),
    ('uZoomParam', union_anon_458),
    ('fnDownloadFileCallBack', DOWNLOAD_DATA_CB),
    ('pUser', POINTER(None)),
    ('byRes', BYTE * 372),
])

NET_DVR_START_PICTURE_FROM_CLOUD_COND = struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_COND
LPNET_DVR_START_PICTURE_FROM_CLOUD_COND = POINTER(struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_COND)
tagNET_DVR_START_PICTURE_FROM_CLOUD_COND = struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_COND
