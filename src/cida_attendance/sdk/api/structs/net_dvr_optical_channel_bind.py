from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPTICAL_CHANNEL_BIND(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_CHANNEL_BIND, [
    ('wChannelIndex', WORD),
    ('wSubChannel', WORD),
    ('byBind', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_OPTICAL_CHANNEL_BIND = struct_tagNET_DVR_OPTICAL_CHANNEL_BIND
LPNET_DVR_OPTICAL_CHANNEL_BIND = POINTER(struct_tagNET_DVR_OPTICAL_CHANNEL_BIND)
tagNET_DVR_OPTICAL_CHANNEL_BIND = struct_tagNET_DVR_OPTICAL_CHANNEL_BIND
