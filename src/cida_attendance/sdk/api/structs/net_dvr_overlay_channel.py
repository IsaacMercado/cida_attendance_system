from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OVERLAY_CHANNEL(Structure):
    pass

_S(struct_tagNET_DVR_OVERLAY_CHANNEL, [
    ('byChannel', BYTE * 64),
    ('dwDelayTime', DWORD),
    ('byEnableDelayTime', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_OVERLAY_CHANNEL = struct_tagNET_DVR_OVERLAY_CHANNEL
LPNET_DVR_OVERLAY_CHANNEL = POINTER(struct_tagNET_DVR_OVERLAY_CHANNEL)
tagNET_DVR_OVERLAY_CHANNEL = struct_tagNET_DVR_OVERLAY_CHANNEL
