from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SYN_CHANNEL_NAME_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SYN_CHANNEL_NAME_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SYN_CHANNEL_NAME_PARAM = struct_tagNET_DVR_SYN_CHANNEL_NAME_PARAM
LPNET_DVR_SYN_CHANNEL_NAME_PARAM = POINTER(struct_tagNET_DVR_SYN_CHANNEL_NAME_PARAM)
tagNET_DVR_SYN_CHANNEL_NAME_PARAM = struct_tagNET_DVR_SYN_CHANNEL_NAME_PARAM
