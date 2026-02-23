from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RTMP_COND(Structure):
    pass

_S(struct_tagNET_DVR_RTMP_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byStreamType', BYTE),
    ('byRes', BYTE * 303),
])

NET_DVR_RTMP_COND = struct_tagNET_DVR_RTMP_COND
LPNET_DVR_RTMP_COND = POINTER(struct_tagNET_DVR_RTMP_COND)
tagNET_DVR_RTMP_COND = struct_tagNET_DVR_RTMP_COND
