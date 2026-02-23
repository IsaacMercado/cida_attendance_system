from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAMING_COND(Structure):
    pass

_S(struct_tagNET_DVR_STREAMING_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byStreamType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_STREAMING_COND = struct_tagNET_DVR_STREAMING_COND
LPNET_DVR_STREAMING_COND = POINTER(struct_tagNET_DVR_STREAMING_COND)
tagNET_DVR_STREAMING_COND = struct_tagNET_DVR_STREAMING_COND
