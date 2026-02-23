from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEFAULT_VIDEO_COND(Structure):
    pass

_S(struct_tagNET_DVR_DEFAULT_VIDEO_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwVideoMode', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_DEFAULT_VIDEO_COND = struct_tagNET_DVR_DEFAULT_VIDEO_COND
LPNET_DVR_DEFAULT_VIDEO_COND = POINTER(struct_tagNET_DVR_DEFAULT_VIDEO_COND)
tagNET_DVR_DEFAULT_VIDEO_COND = struct_tagNET_DVR_DEFAULT_VIDEO_COND
