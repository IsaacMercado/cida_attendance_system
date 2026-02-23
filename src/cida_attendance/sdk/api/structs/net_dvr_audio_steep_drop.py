from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_STEEP_DROP(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_STEEP_DROP, [
    ('bySensitivity', BYTE),
    ('byEnable', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_AUDIO_STEEP_DROP = struct_tagNET_DVR_AUDIO_STEEP_DROP
LPNET_DVR_AUDIO_STEEP_DROP = POINTER(struct_tagNET_DVR_AUDIO_STEEP_DROP)
tagNET_DVR_AUDIO_STEEP_DROP = struct_tagNET_DVR_AUDIO_STEEP_DROP
