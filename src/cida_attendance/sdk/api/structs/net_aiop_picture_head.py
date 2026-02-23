from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_system_time import NET_DVR_SYSTEM_TIME


class struct__NET_AIOP_PICTURE_HEAD_(Structure):
    pass

_S(struct__NET_AIOP_PICTURE_HEAD_, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_SYSTEM_TIME),
    ('szPID', c_char * 64),
    ('dwAIOPDataSize', DWORD),
    ('byStatus', BYTE),
    ('byPictureMode', BYTE),
    ('byRes1', BYTE * 2),
    ('szMPID', c_char * 64),
    ('pBufferAIOPData', POINTER(BYTE)),
    ('dwPresetIndex', DWORD),
    ('dwPictureSize', DWORD),
    ('pBufferPicture', POINTER(BYTE)),
    ('szTaskID', c_char * 64),
    ('byRes', BYTE * 104),
])

NET_AIOP_PICTURE_HEAD = struct__NET_AIOP_PICTURE_HEAD_
LPNET_AIOP_PICTURE_HEAD = POINTER(struct__NET_AIOP_PICTURE_HEAD_)
_NET_AIOP_PICTURE_HEAD_ = struct__NET_AIOP_PICTURE_HEAD_
