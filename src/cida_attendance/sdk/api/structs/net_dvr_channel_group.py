from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANNEL_GROUP(Structure):
    pass

_S(struct_tagNET_DVR_CHANNEL_GROUP, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwGroup', DWORD),
    ('byID', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPositionNo', DWORD),
    ('byRes', BYTE * 56),
])

NET_DVR_CHANNEL_GROUP = struct_tagNET_DVR_CHANNEL_GROUP
LPNET_DVR_CHANNEL_GROUP = POINTER(struct_tagNET_DVR_CHANNEL_GROUP)
tagNET_DVR_CHANNEL_GROUP = struct_tagNET_DVR_CHANNEL_GROUP
