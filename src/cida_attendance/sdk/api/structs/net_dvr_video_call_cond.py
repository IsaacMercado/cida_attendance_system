from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_CALL_COND(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_CALL_COND, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_VIDEO_CALL_COND = struct_tagNET_DVR_VIDEO_CALL_COND
LPNET_DVR_VIDEO_CALL_COND = POINTER(struct_tagNET_DVR_VIDEO_CALL_COND)
tagNET_DVR_VIDEO_CALL_COND = struct_tagNET_DVR_VIDEO_CALL_COND
