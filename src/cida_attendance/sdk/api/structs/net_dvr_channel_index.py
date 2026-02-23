from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANNEL_INDEX(Structure):
    pass

_S(struct_tagNET_DVR_CHANNEL_INDEX, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwIndex', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_CHANNEL_INDEX = struct_tagNET_DVR_CHANNEL_INDEX
LPNET_DVR_CHANNEL_INDEX = POINTER(struct_tagNET_DVR_CHANNEL_INDEX)
tagNET_DVR_CHANNEL_INDEX = struct_tagNET_DVR_CHANNEL_INDEX
