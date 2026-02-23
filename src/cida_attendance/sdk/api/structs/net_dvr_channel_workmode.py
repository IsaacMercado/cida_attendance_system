from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANNEL_WORKMODE(Structure):
    pass

_S(struct_tagNET_DVR_CHANNEL_WORKMODE, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_CHANNEL_WORKMODE = struct_tagNET_DVR_CHANNEL_WORKMODE
LPNET_DVR_CHANNEL_WORKMODE = POINTER(struct_tagNET_DVR_CHANNEL_WORKMODE)
tagNET_DVR_CHANNEL_WORKMODE = struct_tagNET_DVR_CHANNEL_WORKMODE
