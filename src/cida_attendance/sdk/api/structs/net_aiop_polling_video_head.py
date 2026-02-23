from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_system_time import NET_DVR_SYSTEM_TIME


class struct__NET_AIOP_POLLING_VIDEO_HEAD_(Structure):
    pass

_S(struct__NET_AIOP_POLLING_VIDEO_HEAD_, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struTime', NET_DVR_SYSTEM_TIME),
    ('szTaskID', c_char * 64),
    ('dwAIOPDataSize', DWORD),
    ('dwPictureSize', DWORD),
    ('szMPID', c_char * 64),
    ('pBufferAIOPData', POINTER(BYTE)),
    ('pBufferPicture', POINTER(BYTE)),
    ('byPictureMode', BYTE),
    ('byRes2', BYTE * 3),
    ('dwPresetIndex', DWORD),
    ('byRes', BYTE * 176),
])

NET_AIOP_POLLING_VIDEO_HEAD = struct__NET_AIOP_POLLING_VIDEO_HEAD_
LPNET_AIOP_POLLING_VIDEO_HEAD = POINTER(struct__NET_AIOP_POLLING_VIDEO_HEAD_)
_NET_AIOP_POLLING_VIDEO_HEAD_ = struct__NET_AIOP_POLLING_VIDEO_HEAD_
