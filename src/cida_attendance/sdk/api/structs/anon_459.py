from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_anon_459(Structure):
    pass

_S(struct_anon_459, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('dwPicLen', DWORD),
    ('byPicType', BYTE),
    ('byRes', BYTE * 107),
])

NET_DVR_PICTURE_FROM_CLOUD_RET = struct_anon_459
LPNET_DVR_PICTURE_FROM_CLOUD_RET = POINTER(struct_anon_459)
