from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_INFO, [
    ('dwSize', DWORD),
    ('byID', BYTE * 32),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_STREAM_INFO = struct_tagNET_DVR_STREAM_INFO
LPNET_DVR_STREAM_INFO = POINTER(struct_tagNET_DVR_STREAM_INFO)
tagNET_DVR_STREAM_INFO = struct_tagNET_DVR_STREAM_INFO
