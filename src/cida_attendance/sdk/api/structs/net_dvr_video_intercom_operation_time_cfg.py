from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_intercom_operation_time_union import (
    NET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION,
)


class struct_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG, [
    ('dwSize', DWORD),
    ('byUnitType', BYTE),
    ('byRes1', BYTE * 3),
    ('uVideoIntercomUnit', NET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION),
    ('byRes2', BYTE * 128),
])

NET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG
LPNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG)
tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_CFG
