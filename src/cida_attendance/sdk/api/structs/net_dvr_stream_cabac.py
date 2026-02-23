from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_CABAC(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_CABAC, [
    ('dwSize', DWORD),
    ('byCabacEnable', BYTE),
    ('byRes1', BYTE * 31),
])

NET_DVR_STREAM_CABAC = struct_tagNET_DVR_STREAM_CABAC
LPNET_DVR_STREAM_CABAC = POINTER(struct_tagNET_DVR_STREAM_CABAC)
tagNET_DVR_STREAM_CABAC = struct_tagNET_DVR_STREAM_CABAC
