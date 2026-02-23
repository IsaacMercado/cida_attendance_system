from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OUTPUT_VIDEO_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_VIDEO_TYPE, [
    ('dwSize', DWORD),
    ('byType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_OUTPUT_VIDEO_TYPE = struct_tagNET_DVR_OUTPUT_VIDEO_TYPE
LPNET_DVR_OUTPUT_VIDEO_TYPE = POINTER(struct_tagNET_DVR_OUTPUT_VIDEO_TYPE)
tagNET_DVR_OUTPUT_VIDEO_TYPE = struct_tagNET_DVR_OUTPUT_VIDEO_TYPE
