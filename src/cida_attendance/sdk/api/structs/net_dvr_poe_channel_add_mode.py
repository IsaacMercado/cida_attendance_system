from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POE_CHANNEL_ADD_MODE(Structure):
    pass

_S(struct_tagNET_DVR_POE_CHANNEL_ADD_MODE, [
    ('dwSize', DWORD),
    ('byAddMode', BYTE),
    ('byRes1', BYTE * 127),
])

NET_DVR_POE_CHANNEL_ADD_MODE = struct_tagNET_DVR_POE_CHANNEL_ADD_MODE
LPNET_DVR_POE_CHANNEL_ADD_MODE = POINTER(struct_tagNET_DVR_POE_CHANNEL_ADD_MODE)
tagNET_DVR_POE_CHANNEL_ADD_MODE = struct_tagNET_DVR_POE_CHANNEL_ADD_MODE
