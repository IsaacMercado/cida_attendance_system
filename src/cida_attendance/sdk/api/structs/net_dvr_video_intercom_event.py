from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_dvr_video_intercom_event_info_uinon import (
    NET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON,
)


class struct_tagNET_DVR_VIDEO_INTERCOM_EVENT(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_EVENT, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_EX),
    ('byDevNumber', BYTE * 32),
    ('byEventType', BYTE),
    ('byPicTransType', BYTE),
    ('byRes1', BYTE * 2),
    ('uEventInfo', NET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON),
    ('dwIOTChannelNo', DWORD),
    ('byRes2', BYTE * 252),
])

NET_DVR_VIDEO_INTERCOM_EVENT = struct_tagNET_DVR_VIDEO_INTERCOM_EVENT
LPNET_DVR_VIDEO_INTERCOM_EVENT = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_EVENT)
tagNET_DVR_VIDEO_INTERCOM_EVENT = struct_tagNET_DVR_VIDEO_INTERCOM_EVENT
